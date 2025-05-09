# apps/follows/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def send_follow_notification_email(followed_id, follower_id):
    try:
        followed = User.objects.get(id=followed_id)
        follower = User.objects.get(id=follower_id)
    except User.DoesNotExist:
        return
     # Adicionando logs para verificar se a tarefa está sendo chamada corretamente
    print(f"Enviando notificação para {followed.username} sobre o seguidor {follower.username}")
    
    subject = f"Você tem um novo seguidor!"
    message = f"{follower.username} começou a te seguir no Mini-Twitter."
    recipient_list = [followed.email]

    send_mail(subject, message, 'no-reply@minitwitter.com', recipient_list)
