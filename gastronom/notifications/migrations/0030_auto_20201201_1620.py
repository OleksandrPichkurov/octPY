# Generated by Django 2.2 on 2020-12-01 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0029_notification_is_sent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telegramuser',
            old_name='telegram_user_phone',
            new_name='user_phone',
        ),
        migrations.RenameField(
            model_name='telegramuser',
            old_name='telegram_user_name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='user_first_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='First name'),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='user_last_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Last name'),
        ),
    ]
