from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Definindo o módulo de configuração do Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mini_twitter.settings')
app = Celery('mini_twitter')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()