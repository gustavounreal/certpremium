from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        # Registra signals (ex.: login failed) sem acoplamento no settings.
        from . import signals  # noqa: F401
