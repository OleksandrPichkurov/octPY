# Generated by Django 2.2 on 2020-11-28 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0022_telegramincomemessage_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='telegramincomemessage',
            name='text',
            field=models.TextField(max_length=500, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='telegramreplymessage',
            name='reply_message',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='telegram_user_name',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='Telegram User Name'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='telegram_user_phone',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='Telegram user phone number'),
        ),
    ]
