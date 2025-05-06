from django.db import models
from django.contrib.auth import get_user_model
from simple_history.models import HistoricalRecords
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField

User = get_user_model()

class Follow(models.Model):
    history = AuditlogHistoryField()
    history = HistoricalRecords()
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'followed')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.follower.username} → {self.followed.username}"
auditlog.register(Follow)