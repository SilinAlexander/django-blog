# Generated by Django 3.1.7 on 2021-08-17 15:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0004_auto_20210817_1543'),
        ('main', '0003_auto_20210417_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='followers', through='actions.Follower', to=settings.AUTH_USER_MODEL),
        ),
    ]
