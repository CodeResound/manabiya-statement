# Generated by Django 5.0.7 on 2024-07-28 08:22
from django.db import migrations
from manabiyacentral.utility.helpers import Argon2

def populate_data(apps, schema_editor):
    Users = apps.get_model('authenticate','Users')
    hasher = Argon2()
    hashed_password = hasher.hash_password(password='admin@123')
    Users.objects.create(
        name = 'Chirag Shrestha',
        username = 'admin',
        password = hashed_password,
        email = 'work.chiragshrestha@gmail.com'
    )

def revert_data(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_data, revert_data)
    ]
