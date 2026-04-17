from .views import certmonitor_dashboard


urlpatterns = [
    
    #Dashboard visual (requer login admin)
    path('dashboard/', certmonitor_dashboard, name='dashboard'),
]
