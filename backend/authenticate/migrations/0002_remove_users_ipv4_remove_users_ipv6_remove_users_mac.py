# Generated by Django 5.0 on 2024-07-18 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='ipv4',
        ),
        migrations.RemoveField(
            model_name='users',
            name='ipv6',
        ),
        migrations.RemoveField(
            model_name='users',
            name='mac',
        ),
    ]
