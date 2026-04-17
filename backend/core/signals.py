import logging
import time

from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver


logger = logging.getLogger('certpremium')


def _get_client_ip(request) -> str | None:
    if request is None:
        return None

    xff = request.META.get('HTTP_X_FORWARDED_FOR')
    if xff:
        # Primeiro IP = client original (quando atrás de proxy)
        return xff.split(',')[0].strip() or None

    return request.META.get('REMOTE_ADDR')


@receiver(user_login_failed)
def log_login_failed(sender, credentials, request, **kwargs):
    # Nunca logar senha; apenas identificadores (username/email) se existirem.
    creds = credentials or {}
    username = creds.get('username') or creds.get('email') or ''

    logger.warning('Login failed', extra={
        'event': 'auth_login_failed',
        'ts': time.time(),
        'ip': _get_client_ip(request),
        'username': str(username)[:150],
        'path': getattr(request, 'path', None),
        'user_agent': (request.META.get('HTTP_USER_AGENT') if request else None),
    })
