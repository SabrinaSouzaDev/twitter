from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.follows.models import Follow
from apps.follows.tasks import send_follow_email

@receiver(post_save, sender=Follow)
def notify_followed_user(sender, instance, created, **kwargs):
    if created:
        send_follow_email.delay(instance.followed.email)
