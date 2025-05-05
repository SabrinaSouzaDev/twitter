from celery import shared_task
from django.core.mail import send_mail
from django.core.exceptions import ImproperlyConfigured
from apps.accounts.models import User  # Ou o modelo que você usa para a conta de usuário

@shared_task
def send_follow_email(follower_id, followed_email):
    try:
        # Recupera o usuário seguidor do banco de dados pelo ID
        follower = User.objects.get(id=follower_id)

        # Envia o e-mail usando o e-mail do seguidor como remetente
        send_mail(
            "Alguém te seguiu!",
            f"Confira seu novo seguidor: {follower.username} começou a te seguir!",
            follower.email,  # E-mail dinâmico do seguidor
            [followed_email],
            fail_silently=False
        )
    except User.DoesNotExist:
        print(f"Usuário com ID {follower_id} não encontrado.")
    except ImproperlyConfigured:
        # Se houver problemas com as configurações de e-mail
        print("Erro nas configurações de e-mail.")
    except Exception as e:
        # Caso haja qualquer outro erro ao tentar enviar o e-mail
        print(f"Ocorreu um erro ao enviar o e-mail: {str(e)}")
