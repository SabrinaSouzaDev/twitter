from auditlog.registry import auditlog

from apps.feeds.models import Feed


auditlog.register(Feed)
