import uuid
from django.db import models
from manabiyacentral.models import DateTimeModel

class Users(DateTimeModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255, blank=False, null=False)
    last_login = models.DateTimeField(blank=True, null=True)
    session_at = models.DateTimeField(blank=True, null=True)
    login_attempts = models.SmallIntegerField(default=0, blank=True, null=True)
    ipv4 = models.CharField(max_length=16, blank=True, null=True)
    ipv6 = models.CharField(max_length=40, blank=True, null=True)
    mac = models.CharField(max_length=17, blank=True, null=True)
    cooldown_time = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)
    status_reason = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'users'



