from django.urls import path

from apps.follows.views import FollowView, FollowersListView, FollowingListView

urlpatterns = [
    path('', FollowView.as_view(), name='follow'),  # POST para seguir, DELETE para deixar de seguir
    path('following/', FollowingListView.as_view(), name='following-list'),
    path('followers/', FollowersListView.as_view(), name='followers-list'),
]