from django.urls import path

from .views import certmonitor_dashboard, certmonitor_metrics


urlpatterns = [
    # Dashboard visual (requer login admin)
    path('dashboard/', certmonitor_dashboard, name='dashboard'),

    # API: métricas do CertMonitor (requer admin)
    path('monitor/', certmonitor_metrics, name='certmonitor-metrics'),
]
