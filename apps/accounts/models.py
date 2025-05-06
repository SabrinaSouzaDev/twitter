from django.contrib.auth.models import AbstractUser
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField
from django.db import models


class User(AbstractUser):
    history = AuditlogHistoryField()
    """
    Representa um usuário customizado com informações adicionais como biografia.
    """
    bio = models.TextField(blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        verbose_name='user permissions'
    )

    def __str__(self):
        return str(self.username or "")
    
auditlog.register(User)
