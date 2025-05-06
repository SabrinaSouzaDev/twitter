from django.urls import path
from apps.feeds.views import UserFeedView

urlpatterns = [
    path('user/', UserFeedView.as_view(), name='user-feed'),  # Feed do usuário
]
