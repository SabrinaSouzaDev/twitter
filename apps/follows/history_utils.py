# users/history_utils.py
# from django.contrib.auth.models import User

from apps.accounts.models import User

def listar_historico_usuario(username: str):
    try:
        user = User.objects.get(username=username)
        history = user.history.all()
        for h in history:
            print(h.history_date, h.history_user, h.history_type, h)
    except User.DoesNotExist:
        print(f"Usuário '{username}' não encontrado.")
