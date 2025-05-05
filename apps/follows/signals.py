from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Follow
from .tasks import send_follow_email


@receiver(post_save, sender=Follow)
def send_follow_notification_email(sender, instance, created, **kwargs):
    if created:
        send_follow_email.delay(
            follower_username=instance.follower.username,
            followed_email=instance.followed.email
        )
