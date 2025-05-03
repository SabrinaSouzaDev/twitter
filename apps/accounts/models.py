from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
import os


def validate_image(image):
    """
    Valida se a imagem tem uma extensão permitida (.jpg, .jpeg, .png).
    """
    if not image.name.lower().endswith(('.jpg', '.jpeg', '.png')):
        raise ValidationError("Apenas imagens .jpg, .jpeg e .png são permitidas.")
    return image


class User(AbstractUser):
    """
    Representa um usuário customizado com informações adicionais como
    biografia e imagem de perfil.
    """
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='profiles/', 
        blank=True, 
        null=True, 
        validators=[validate_image]
    )
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


    def save(self, *args, **kwargs):
        """
        Sobrescreve o método save para garantir que o diretório de upload
        da imagem de perfil seja criado, se necessário.
        """
        super().save(*args, **kwargs)
        if self.profile_picture and hasattr(self.profile_picture, 'path'):
            try:
                os.makedirs(os.path.dirname(self.profile_picture.path), exist_ok=True)
            except (OSError, ValueError):
                pass