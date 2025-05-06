# tweets/admin.py

from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from apps.accounts.models import User


@admin.register(User)
class TweetAdmin(SimpleHistoryAdmin):
    pass
