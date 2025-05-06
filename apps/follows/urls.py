from django.urls import path
from .views import (
    FollowUserView,
    UnfollowUserView,
    ListFollowersView,
    ListFollowingView,
)

urlpatterns = [
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('<int:user_id>/followers/', ListFollowersView.as_view(), name='user-followers'),
    path('<int:user_id>/following/', ListFollowingView.as_view(), name='user-following'),
]
