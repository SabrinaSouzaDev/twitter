from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'
    
    def ready(self):
        from .models import User
        from auditlog.registry import auditlog
        auditlog.register(User)
    