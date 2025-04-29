from django.contrib import admin
from django.contrib.auth import get_user_model
from apps.follows.models import Follow

User = get_user_model()

class FollowersInline(admin.TabularInline):
    model = Follow
    fk_name = 'followed'  # Usuário que está sendo seguido
    extra = 0
    verbose_name = "Follower"
    verbose_name_plural = "Followers"

class FollowingInline(admin.TabularInline):
    model = Follow
    fk_name = 'follower'  # Usuário que está seguindo
    extra = 0
    verbose_name = "Following"
    verbose_name_plural = "Following"

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [FollowersInline, FollowingInline]
    # ... outras configurações do admin