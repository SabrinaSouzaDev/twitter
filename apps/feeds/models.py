from django.db import models
from django.conf import settings
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField
# from simple_history.models import HistoricalRecords

class Feed(models.Model):
    history = AuditlogHistoryField()
    # history = HistoricalRecords()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Feed'
        verbose_name_plural = 'Feeds'


class FeedImage(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='feeds/images/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Feed Image'
        verbose_name_plural = 'Feed Images'
        ordering = ['-created_at']