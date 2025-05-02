from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_follow_email(to_email):
    send_mail(
        "Alguém te seguiu!",
        "Confira seu novo seguidor!",
        "no-reply@site.com",
        [to_email],
        fail_silently=False
    )
