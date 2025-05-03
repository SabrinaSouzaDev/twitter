from django.db import models

from apps.accounts.models import User


class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['follower', 'followed'], name='unique_follow')
        ]
    
    def __str__(self):
        return f"{self.follower} segue {self.followed}"

    # método save() para garantir que um usuário não possa seguir a si mesmo
    def save(self, *args, **kwargs):
        if self.follower == self.followed:
            raise ValueError("Você não pode seguir a si mesmo.")
        super().save(*args, **kwargs)