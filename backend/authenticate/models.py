from typing import Any
import uuid
from django.db import models
from manabiyacentral.models import DateTimeModel

class Users(DateTimeModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField()
    last_login = models.DateTimeField(blank=True, null=True)
    session_at = models.DateTimeField(blank=True, null=True)
    login_attempts = models.SmallIntegerField(default=0, blank=True, null=True)
    cooldown_time = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True, blank=True)
    status_reason = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'users'
