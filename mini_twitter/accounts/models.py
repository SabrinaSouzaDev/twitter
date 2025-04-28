from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)

    @property
    def followers_count(self):
        return self.followers.count()