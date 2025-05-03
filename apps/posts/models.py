from django.db import models
from apps.accounts.models import User


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
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
