# Generated by Django 2.2 on 2021-01-31 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group_app', '0003_gameinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameinfo',
            name='gold',
        ),
        migrations.AddField(
            model_name='user',
            name='gold',
            field=models.IntegerField(default=1000),
        ),
    ]
