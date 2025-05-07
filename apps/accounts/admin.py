from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass  # Customize aqui se quiser
    # list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # search_fields = ('username', 'email')
    # list_filter = ('is_staff', 'is_active')
