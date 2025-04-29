from django.urls import path

from apps.follows.views import FollowView, FollowersListView, FollowingListView

urlpatterns = [
    # Seguir/Deixar de seguir
    path('follow/', FollowView.as_view({'post': 'create'}), name='follow-create'),
    path('unfollow/<int:pk>/', FollowView.as_view({'delete': 'destroy'}), name='follow-destroy'),
    
    # Listagens
    path('following/', FollowingListView.as_view(), name='following-list'),
    path('followers/', FollowersListView.as_view(), name='followers-list'),
]