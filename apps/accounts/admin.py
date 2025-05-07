from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.follows.models import Follow
from .models import User


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
class UserAdmin(BaseUserAdmin):
    pass  # Customize aqui se quiser
    # list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # search_fields = ('username', 'email')
    # list_filter = ('is_staff', 'is_active')
