import logging
import os
import time


logger = logging.getLogger('certpremium')


class SecurityRequestLogMiddleware:
    """Loga requests (best effort) para alimentar métricas estilo SIEM.

    Ativo por padrão. Para desativar (reduzir volume de logs):
      CERTMONITOR_HTTP_LOGGING=0
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.enabled = os.getenv('CERTMONITOR_HTTP_LOGGING', '1') == '1'

    def __call__(self, request):
        if not self.enabled:
            return self.get_response(request)

        path = getattr(request, 'path', '') or ''

        # Logar apenas rotas relevantes (reduz ruído/volume)
        should_log = path.startswith('/api/') or path.startswith('/admin/')

        start = time.perf_counter()
        response = self.get_response(request)

        if should_log:
            try:
                duration_ms = (time.perf_counter() - start) * 1000
                xff = request.META.get('HTTP_X_FORWARDED_FOR')
                ip = (xff.split(',')[0].strip() if xff else request.META.get('REMOTE_ADDR'))

                user = getattr(request, 'user', None)
                user_id = getattr(user, 'id', None) if getattr(user, 'is_authenticated', False) else None

                logger.info('HTTP request', extra={
                    'event': 'http_request',
                    'ts': time.time(),
                    'ip': ip,
                    'method': getattr(request, 'method', None),
                    'path': path,
                    'status_code': getattr(response, 'status_code', None),
                    'duration_ms': round(duration_ms, 2),
                    'user_id': str(user_id) if user_id else None,
                })
            except Exception:
                # Nunca quebrar a request por causa de log.
                pass

        return response
