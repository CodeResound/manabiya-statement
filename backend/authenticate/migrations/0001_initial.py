# Generated by Django 5.0.7 on 2024-07-23 10:55

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('createdat', models.DateTimeField(auto_now_add=True)),
                ('updatedat', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('session_at', models.DateTimeField(blank=True, null=True)),
                ('login_attempts', models.SmallIntegerField(blank=True, default=0, null=True)),
                ('cooldown_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(blank=True, default=True)),
                ('status_reason', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
