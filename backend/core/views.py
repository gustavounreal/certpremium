import logging
import psutil
from django.utils import timezone
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication



logger = logging.getLogger('certpremium')


@api_view(['GET'])
@authentication_classes([SessionAuthentication, JWTAuthentication])
@permission_classes([IsAdminUser])
def certmonitor_metrics(request):
    """
    CertMonitor 360 — Métricas de infraestrutura.
    Apenas admins podem acessar (previne reconhecimento).
    """
    logger.info('CertMonitor accessed', extra={
        'user_id': str(request.user.id),
        'ip': request.META.get('REMOTE_ADDR'),
        'event': 'monitor_access'
    })

    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return Response({
        "status": "Healthy",
        "cpu_percent": psutil.cpu_percent(interval=1),
        "ram_used_mb": round(memory.used / (1024 * 1024), 2),
        "ram_total_mb": round(memory.total / (1024 * 1024), 2),
        "ram_percent": memory.percent,
        "disk_free_gb": round(disk.free / (1024 * 1024 * 1024), 2),
        "disk_percent": disk.percent
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
