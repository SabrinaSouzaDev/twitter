from django.apps import AppConfig


class FeedsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.feeds'
    
    
    def ready(self):
        from apps.feeds.models import Feed
        from auditlog.registry import auditlog
        auditlog.register(Feed)