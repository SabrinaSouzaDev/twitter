from django.urls import path
from apps.feeds.views import FeedView

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),
]
