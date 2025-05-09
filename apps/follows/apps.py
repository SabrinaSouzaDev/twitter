from django.apps import AppConfig


class FollowsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.follows'
    
    
    def ready(self):
        import apps.follows.signals
        from .models import Follow
        from auditlog.registry import auditlog
        auditlog.register(Follow)