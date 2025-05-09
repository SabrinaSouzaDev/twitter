# apps/follows/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Follow
from .tasks import send_follow_notification_email

@receiver(post_save, sender=Follow)
def send_follow_email(sender, instance, created, **kwargs):
    if created:
        send_follow_notification_email.delay(instance.followed.id, instance.follower.id)
