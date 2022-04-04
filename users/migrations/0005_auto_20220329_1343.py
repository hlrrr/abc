# Generated by Django 3.2.12 on 2022-03-29 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220329_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='currency',
            field=models.TextField(blank=True, choices=[('usd', 'USD'), ('krw', 'KRW')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='sueprhost',
            field=models.BooleanField(default=False),
        ),
    ]