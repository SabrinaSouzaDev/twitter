from django.db import models
from apps.accounts.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
# from simple_history.models import HistoricalRecords
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField



class Post(models.Model):
    history = AuditlogHistoryField()
    # history = HistoricalRecords()
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    id = models.AutoField(primary_key=True)

    # Tipagem para ajudar o Pylance a reconhecer a relação reversa "likes"
    likes: 'models.QuerySet[PostLike]'

    @property
    def like_count(self) -> int:
        """
        Retorna o número de curtidas associadas à postagem.
        """
        return self.likes.count()

    def __str__(self) -> str:
        return f"{self.author.username}: {self.content[:30]}"  # pylint: disable=unsubscriptable-object

    class Meta:
        ordering = ['-created_at']
auditlog.register(Post)

class PostLike(models.Model):
    """
    Representa uma curtida de um usuário em uma postagem.
    """
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='liked_posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username} curtiu: {self.post.content[:30]}"  # pylint: disable=unsubscriptable-object

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['post', 'user'], name='unique_post_like')
        ]

auditlog.register(PostLike)      
@receiver(post_save, sender=Post)        
def clear_feed_cache(sender, instance, **kwargs):
    cache_key = f"user_feed_{instance.author.pk}"
    cache.delete(cache_key) 