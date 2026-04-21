import json
import logging
import os
import time
from collections import Counter
from datetime import datetime
from ipaddress import ip_address

import psutil
from django.contrib.admin.views.decorators import staff_member_required
from django.db import connection
from django.shortcuts import render
from django.utils import timezone

from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication


logger = logging.getLogger('certpremium')


def _tail_lines(path: str, *, max_lines: int = 200, max_bytes: int = 200_000) -> list[str]:
    """Lê as últimas linhas de um arquivo sem carregar tudo na memória."""
    try:
        with open(path, 'rb') as f:
            f.seek(0, os.SEEK_END)
            size = f.tell()
            start = max(size - max_bytes, 0)
            f.seek(start)
            chunk = f.read()
        text = chunk.decode('utf-8', errors='replace')
        lines = text.splitlines()
        return lines[-max_lines:]
    except FileNotFoundError:
        return []
    except OSError:
        return []


def _read_recent_events(*, max_events: int = 10) -> list[dict]:
    """Extrai eventos recentes do log JSON (best effort)."""
    log_path = os.getenv('CERTMONITOR_LOG_FILE', '/app/logs/api.json')
    lines = _tail_lines(log_path)

    events: list[dict] = []
    for line in reversed(lines):
        try:
            rec = json.loads(line)
        except Exception:
            continue

        event = rec.get('event')
        if not event or event == 'monitor_access':
            continue

        events.append({
            'at': rec.get('asctime'),
            'level': rec.get('levelname'),
            'event': event,
            'message': rec.get('message'),
            'user_id': rec.get('user_id'),
            'ip': rec.get('ip'),
        })

        if len(events) >= max_events:
            break

    return list(reversed(events))


def _db_healthcheck() -> tuple[bool, float | None, str | None]:
    """Checa conectividade do PostgreSQL e mede latência (ms)."""
    try:
        start = time.perf_counter()
        with connection.cursor() as cur:
            cur.execute('SELECT 1;')
            cur.fetchone()
        latency_ms = (time.perf_counter() - start) * 1000
        return True, round(latency_ms, 2), None
    except Exception:
        logger.exception('Database healthcheck failed')
        return False, None, 'Database healthcheck failed'


def _read_siem_summary(*, max_lines: int = 200) -> dict:
    """Resumo estilo SIEM a partir do log JSON (best effort).

    A ideia é dar sinais do "estado de segurança" (erros/avisos, eventos, IPs) sem
    depender de ferramentas externas.
    """
    log_path = os.getenv('CERTMONITOR_LOG_FILE', '/app/logs/api.json')
    lines = _tail_lines(log_path, max_lines=max_lines)

    if not lines:
        return {
            'available': False,
            'log_path': log_path,
            'sample_lines': 0,
            'parsed_lines': 0,
            'levels': {},
            'top_events': [],
            'top_ips': [],
            'last_error_at': None,
            'message': 'Log não encontrado ou vazio',
        }

    levels: dict[str, int] = {}
    events: dict[str, int] = {}
    ips: dict[str, int] = {}

    parsed_lines = 0
    last_error_at: str | None = None

    for line in lines:
        try:
            rec = json.loads(line)
        except Exception:
            continue

        parsed_lines += 1

        level = rec.get('levelname')
        if level:
            level = str(level).upper()
            levels[level] = levels.get(level, 0) + 1

        event = rec.get('event')
        if event:
            event = str(event)
            events[event] = events.get(event, 0) + 1

        ip = rec.get('ip')
        if ip:
            ip = str(ip)
            ips[ip] = ips.get(ip, 0) + 1

        if level in ('ERROR', 'CRITICAL'):
            last_error_at = rec.get('asctime') or last_error_at

    top_events = [
        {'event': k, 'count': v}
        for k, v in sorted(events.items(), key=lambda kv: kv[1], reverse=True)[:5]
    ]
    top_ips = [
        {'ip': k, 'count': v}
        for k, v in sorted(ips.items(), key=lambda kv: kv[1], reverse=True)[:5]
    ]

    return {
        'available': True,
        'log_path': log_path,
        'sample_lines': len(lines),
        'parsed_lines': parsed_lines,
        'levels': levels,
        'top_events': top_events,
        'top_ips': top_ips,
        'last_error_at': last_error_at,
    }


def _read_blocked_ips(*, max_ips: int = 50) -> dict:
    """IPs bloqueados (Fail2ban/CrowdSec) via arquivo (best effort).

    Configure um arquivo (montado no container) com 1 IP por linha e aponte via:
      CERTMONITOR_BLOCKED_IPS_FILE=/caminho/blocked_ips.txt

    Isso evita chamar binários externos dentro da API.
    """
    path = os.getenv('CERTMONITOR_BLOCKED_IPS_FILE')
    if not path:
        return {
            'available': False,
            'count': 0,
            'ips': [],
            'source': None,
            'message': 'Configure CERTMONITOR_BLOCKED_IPS_FILE para exibir IPs bloqueados',
        }

    ips: list[str] = []
    seen: set[str] = set()

    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            for line in f:
                raw = line.strip()
                if not raw or raw.startswith('#'):
                    continue

                token = raw.split()[0]
                try:
                    ip = str(ip_address(token))
                except ValueError:
                    continue

                if ip in seen:
                    continue
                seen.add(ip)
                ips.append(ip)

                if len(ips) >= max_ips:
                    break

        return {
            'available': True,
            'count': len(ips),
            'ips': ips,
            'source': path,
        }
    except FileNotFoundError:
        return {
            'available': False,
            'count': 0,
            'ips': [],
            'source': path,
            'message': 'Arquivo de blocklist não encontrado',
        }
    except OSError:
        return {
            'available': False,
            'count': 0,
            'ips': [],
            'source': path,
            'message': 'Sem permissão para ler a blocklist',
        }


def _read_security_metrics(*, max_lines: int = 2000) -> dict:
    """Métricas de segurança (best effort) a partir de logs estruturados."""
    log_path = os.getenv('CERTMONITOR_LOG_FILE', '/app/logs/api.json')
    now = time.time()

    lines = _tail_lines(log_path, max_lines=max_lines, max_bytes=2_000_000)

    parsed: list[dict] = []
    for line in lines:
        try:
            rec = json.loads(line)
        except Exception:
            continue
        if isinstance(rec, dict):
            parsed.append(rec)

    def rec_ts(rec: dict) -> float | None:
        ts = rec.get('ts')
        if isinstance(ts, (int, float)):
            return float(ts)

        # Fallback: tenta parsear asctime (pode falhar dependendo do formatter)
        asctime = rec.get('asctime')
        if not asctime:
            return None

        for fmt in ('%Y-%m-%d %H:%M:%S,%f', '%Y-%m-%d %H:%M:%S'):
            try:
                dt = datetime.strptime(str(asctime), fmt)
                return dt.timestamp()
            except Exception:
                continue

        return None

    def in_window(ts: float | None, seconds: int) -> bool:
        return ts is not None and ts >= (now - seconds)

    failed_5m = 0
    failed_1h = 0
    failed_ips_1h: Counter[str] = Counter()

    req_1m = 0
    req_15m = 0

    req_ips_1m: Counter[str] = Counter()

    errors_5m = 0

    for rec in parsed:
        ts = rec_ts(rec)
        ev = rec.get('event')
        ip = rec.get('ip')

        if ev == 'auth_login_failed':
            if in_window(ts, 300):
                failed_5m += 1
            if in_window(ts, 3600):
                failed_1h += 1
                if ip:
                    failed_ips_1h[str(ip)] += 1

        if ev == 'http_request':
            if in_window(ts, 60):
                req_1m += 1
                if ip:
                    req_ips_1m[str(ip)] += 1

            # baseline: últimos 16min menos último 1min
            if ts is not None and (now - 16 * 60) <= ts < (now - 60):
                req_15m += 1

        level = rec.get('levelname')
        if level and in_window(ts, 300):
            level = str(level).upper()
            if level in ('ERROR', 'CRITICAL'):
                errors_5m += 1

    baseline_per_min_15m = round((req_15m / 15.0), 2) if req_15m > 0 else 0.0
    spike_factor = round((req_1m / baseline_per_min_15m), 2) if baseline_per_min_15m > 0 else None

    spike_detected = bool(spike_factor is not None and req_1m >= 30 and spike_factor >= 3)

    blocked = _read_blocked_ips()
    blocked_count = int(blocked.get('count') or 0)

    # Anomaly score (heurístico 0-100)
    score = 0.0
    score += min(40.0, failed_5m * 4.0)
    if spike_factor is not None and spike_factor > 1:
        score += min(30.0, (spike_factor - 1.0) * 10.0)
    score += min(30.0, errors_5m * 5.0)
    score += min(10.0, float(blocked_count))
    score = min(100.0, score)

    anomaly_score = int(round(score))
    if anomaly_score >= 75:
        anomaly_label = 'Crítico'
    elif anomaly_score >= 50:
        anomaly_label = 'Alto'
    elif anomaly_score >= 25:
        anomaly_label = 'Médio'
    else:
        anomaly_label = 'Baixo'

    top_failed_ips = [{'ip': k, 'count': v} for k, v in failed_ips_1h.most_common(5)]
    top_req_ips = [{'ip': k, 'count': v} for k, v in req_ips_1m.most_common(5)]

    return {
        'log_path': log_path,
        'log_lines_sampled': len(lines),
        'failed_login_attempts_5m': failed_5m,
        'failed_login_attempts_1h': failed_1h,
        'top_failed_login_ips_1h': top_failed_ips,
        'request_rate_1m': req_1m,
        'request_rate_baseline_15m': baseline_per_min_15m,
        'request_spike_factor': spike_factor,
        'request_spike_detected': spike_detected,
        'top_request_ips_1m': top_req_ips,
        'errors_5m': errors_5m,
        'blocked_ips': blocked,
        'anomaly_score': anomaly_score,
        'anomaly_label': anomaly_label,
        'notes': {
            'http_logging_default_on': 'Logging HTTP ativo por padrão (spikes/taxa). Desative com CERTMONITOR_HTTP_LOGGING=0.',
            'blocked_ips_opt_in': 'Configure CERTMONITOR_BLOCKED_IPS_FILE (ex.: export de Fail2ban/CrowdSec).',
        },
    }


def _compute_status_details(
    *,
    cpu: float,
    ram: float,
    disk: float,
    swap: float,
    db_ok: bool,
    db_latency_ms: float | None,
    security: dict | None,
) -> tuple[str, str, str, list[dict]]:
    """Retorna status + explicação (motivos) em pt-BR."""

    reasons: list[dict] = []

    def add_reason(severity: str, title: str, detail: str):
        reasons.append({'severity': severity, 'title': title, 'detail': detail})

    def check_percent(name: str, value: float, warn: float, crit: float):
        if value >= crit:
            add_reason('critical', name, f'{value:.1f}% (crítico ≥ {crit:.0f}%)')
        elif value >= warn:
            add_reason('warning', name, f'{value:.1f}% (atenção ≥ {warn:.0f}%)')

    check_percent('CPU alta', cpu, 70, 90)
    check_percent('RAM alta', ram, 70, 90)
    check_percent('Disco alto', disk, 80, 90)
    check_percent('Swap alta', swap, 20, 50)

    if not db_ok:
        add_reason('critical', 'Banco indisponível', 'Falha ao executar SELECT 1')
    elif db_latency_ms is not None:
        if db_latency_ms >= 1000:
            add_reason('critical', 'Banco lento', f'{db_latency_ms:.0f} ms (crítico ≥ 1000 ms)')
        elif db_latency_ms >= 200:
            add_reason('warning', 'Banco lento', f'{db_latency_ms:.0f} ms (atenção ≥ 200 ms)')

    sec = security or {}

    failed_5m = int(sec.get('failed_login_attempts_5m') or 0)
    if failed_5m >= 20:
        add_reason('critical', 'Brute force (login)', f'{failed_5m} falhas em 5 min')
    elif failed_5m >= 5:
        add_reason('warning', 'Muitas falhas de login', f'{failed_5m} falhas em 5 min')

    spike = sec.get('request_spike_factor')
    req_1m = int(sec.get('request_rate_1m') or 0)
    baseline = float(sec.get('request_rate_baseline_15m') or 0)
    if spike is not None:
        try:
            spike_f = float(spike)
        except Exception:
            spike_f = None

        if spike_f is not None and req_1m >= 30 and spike_f >= 6:
            add_reason('critical', 'Pico de requisições', f'{req_1m} req/min vs {baseline:.2f}/min ({spike_f:.1f}x)')
        elif spike_f is not None and req_1m >= 30 and spike_f >= 3:
            add_reason('warning', 'Pico de requisições', f'{req_1m} req/min vs {baseline:.2f}/min ({spike_f:.1f}x)')

    blocked = sec.get('blocked_ips') or {}
    blocked_count = int(blocked.get('count') or 0) if isinstance(blocked, dict) else 0
    if blocked_count > 0:
        add_reason('warning', 'IPs bloqueados', f'{blocked_count} IP(s) em blocklist (Fail2ban/CrowdSec)')

    anomaly_score = int(sec.get('anomaly_score') or 0)
    if anomaly_score >= 90:
        add_reason('critical', 'Anomalia', f'Score {anomaly_score}/100')
    elif anomaly_score >= 75:
        add_reason('warning', 'Anomalia', f'Score {anomaly_score}/100')

    status_code = 'healthy'
    status_label = 'Saudável'

    if any(r['severity'] == 'critical' for r in reasons):
        status_code = 'critical'
        status_label = 'Crítico'
    elif any(r['severity'] == 'warning' for r in reasons):
        status_code = 'warning'
        status_label = 'Atenção'

    if not reasons:
        hint = 'Tudo dentro do esperado.'
    else:
        titles = [r.get('title') for r in reasons if r.get('title')]
        hint = 'Motivo: ' + ', '.join(titles[:3])
        if len(titles) > 3:
            hint += f' (+{len(titles) - 3})'

    return status_code, status_label, hint, reasons


@api_view(['GET'])
@authentication_classes([SessionAuthentication, JWTAuthentication])
@permission_classes([IsAdminUser])
def certmonitor_metrics(request):
    """CertMonitor 360 — Métricas de infraestrutura (admin only)."""
    logger.info('CertMonitor accessed', extra={
        'user_id': str(request.user.id),
        'ip': request.META.get('REMOTE_ADDR'),
        'event': 'monitor_access',
    })

    cpu_percent = float(psutil.cpu_percent(interval=0.1))

    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    disk = psutil.disk_usage('/')
    net = psutil.net_io_counters()

    uptime_seconds = int(time.time() - psutil.boot_time())

    try:
        load_1m, load_5m, load_15m = os.getloadavg()
        load = (round(load_1m, 2), round(load_5m, 2), round(load_15m, 2))
    except OSError:
        load = (None, None, None)

    db_ok, db_latency_ms, db_error = _db_healthcheck()

    security = _read_security_metrics()

    status_code, status_label, status_hint, status_reasons = _compute_status_details(
        cpu=cpu_percent,
        ram=float(memory.percent),
        disk=float(disk.percent),
        swap=float(swap.percent),
        db_ok=db_ok,
        db_latency_ms=db_latency_ms,
        security=security,
    )

    siem_summary = _read_siem_summary()

    proc = psutil.Process(os.getpid())
    proc_rss_mb = round(proc.memory_info().rss / (1024 * 1024), 2)

    return Response({
        'status_code': status_code,
        'status_label': status_label,
        'status_hint': status_hint,
        'status_reasons': status_reasons,
        'siem_summary': siem_summary,
        'security': security,
        'checked_at': timezone.now().isoformat(),

        'cpu_percent': round(cpu_percent, 1),

        'ram_percent': round(float(memory.percent), 1),
        'ram_used_mb': round(memory.used / (1024 * 1024), 2),
        'ram_total_mb': round(memory.total / (1024 * 1024), 2),

        'swap_percent': round(float(swap.percent), 1),
        'swap_used_mb': round(swap.used / (1024 * 1024), 2),
        'swap_total_mb': round(swap.total / (1024 * 1024), 2),

        'disk_percent': round(float(disk.percent), 1),
        'disk_free_gb': round(disk.free / (1024 * 1024 * 1024), 2),
        'disk_total_gb': round(disk.total / (1024 * 1024 * 1024), 2),

        'uptime_seconds': uptime_seconds,
        'load_avg_1m': load[0],
        'load_avg_5m': load[1],
        'load_avg_15m': load[2],

        'net_rx_mb': round(net.bytes_recv / (1024 * 1024), 2),
        'net_tx_mb': round(net.bytes_sent / (1024 * 1024), 2),

        'process_rss_mb': proc_rss_mb,
        'process_threads': proc.num_threads(),

        'db_ok': db_ok,
        'db_latency_ms': db_latency_ms,
        'db_error': db_error,

        'events': _read_recent_events(),
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_data_export(request):
    """
    LGPD Art. 18 — Direito de Portabilidade.
    Permite ao usuário exportar todos os seus dados.
    """
    user = request.user

    logger.info('LGPD data export requested', extra={
        'user_id': str(user.id),
        'ip': request.META.get('REMOTE_ADDR'),
        'event': 'lgpd_export'
    })

    user_data = {
        'profile': {
            'id': str(user.id),
            'username': user.username,
            'email': user.email,
            'date_joined': user.date_joined.isoformat(),
            'is_premium': user.is_premium,
        },
        'progress': list(
            user.userprogress_set.values('last_login', 'streak_days')
        ),
    }

    return Response({
        'status': 'success',
        'message': 'Dados exportados conforme LGPD Art. 18',
        'data': user_data,
        'exported_at': timezone.now().isoformat()
    })


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def user_data_delete(request):
    """
    LGPD Art. 18 — Direito de Eliminação.
    Remove todos os dados do usuário permanentemente.
    """
    user = request.user
    user_id = str(user.id)
    user_email = user.email

    # Exige confirmação explícita
    confirm = request.data.get('confirm', False)
    if not confirm:
        return Response({
            'status': 'confirmation_required',
            'message': 'Envie {"confirm": true} para confirmar exclusão'
        }, status=400)

    logger.warning('LGPD data deletion', extra={
        'user_id': user_id,
        'email': user_email,
        'ip': request.META.get('REMOTE_ADDR'),
        'event': 'lgpd_delete'
    })

    user.delete()

    return Response({
        'status': 'success',
        'message': 'Dados removidos conforme LGPD Art. 18'
    })



@staff_member_required
def certmonitor_dashboard(request):
    """
    Dashboard visual do CertMonitor 360.
    Apenas staff pode acessar.
    """
    return render(request, 'core/certmonitor.html')
