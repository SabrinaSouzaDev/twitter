from django.db import models
from django.conf import settings

class Feed(models.Model):  # Nome no singular
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # outros campos...

    class Meta:
        verbose_name = 'Feed'
        verbose_name_plural = 'Feeds'  # Plural definido aqui