# tweets/admin.py

from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from apps.follows.models import Follow

@admin.register(Follow)
class TweetAdmin(SimpleHistoryAdmin):
    pass
