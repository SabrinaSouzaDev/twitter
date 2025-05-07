# apps/follows/admin.py

from django.contrib import admin
from .models import Follow
from auditlog.models import LogEntry
from auditlog.admin import LogEntryAdmin

# Modelo principal
@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'followed', 'created_at')
    search_fields = ('follower__username', 'followed__username')
    list_filter = ('created_at',)

admin.site.unregister(LogEntry)
admin.site.register(LogEntry, LogEntryAdmin)