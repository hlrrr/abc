# Generated by Django 3.2.12 on 2022-04-08 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='rooms',
            new_name='room',
        ),
    ]
