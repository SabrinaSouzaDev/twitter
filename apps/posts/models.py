from django.db import models

from apps.accounts.models import User


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def like_count(self):
        return self.likes.count()

    class Meta:
        ordering = ['-created_at']

class PostLike(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='liked_posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    constraints = [
        models.UniqueConstraint(fields=['post', 'user'], name='unique_post_like')
    ]

def __str__(self):
    return f"{self.user.username}: {self.content[:30]}"