# Generated by Django 2.2 on 2020-11-26 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0012_auto_20201126_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.PositiveIntegerField(unique=True, verbose_name='Telegram User ID')),
                ('telegram_user_name', models.TextField(blank=True, null=True, verbose_name='Telegram User Name')),
                ('telegram_user_phone', models.TextField(blank=True, null=True, verbose_name='Telegram user phone number')),
            ],
        ),
        migrations.AddField(
            model_name='notification',
            name='subject',
            field=models.TextField(default='GASTRONOM info', max_length=50),
        ),
        migrations.AlterField(
            model_name='notification',
            name='send_method',
            field=models.CharField(choices=[('email', 'E-mail'), ('telegram', 'Telegram'), ('viber', 'Viber'), ('sms', 'Sms'), ('site', 'Site')], default='email', max_length=20),
        ),
        migrations.CreateModel(
            name='TelegramIncomeMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Send time')),
                ('telegramuser', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='notifications.TelegramUser')),
            ],
            options={
                'verbose_name': 'Telegram income message',
            },
        ),
    ]
