# Generated by Django 3.2.12 on 2022-04-15 03:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0004_auto_20220405_1617'),
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lists',
            new_name='List',
        ),
    ]