from django.db import models
from django.conf import settings

class Feed(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Feed'
        verbose_name_plural = 'Feeds'