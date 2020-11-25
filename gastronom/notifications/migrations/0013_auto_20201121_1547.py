# Generated by Django 2.2 on 2020-11-21 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0012_auto_20201120_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='source',
            field=models.CharField(choices=[('rest_framework', 'rest_framework'), ('user_profile', 'user_profile'), ('jet', 'jet'), ('comments.apps.CommentsConfig', 'comments.apps.CommentsConfig'), ('notifications', 'notifications'), ('catalog', 'catalog'), ('product.apps.ProductConfig', 'product.apps.ProductConfig'), ('django.contrib.admin', 'django.contrib.admin'), ('django.contrib.auth', 'django.contrib.auth'), ('django.contrib.contenttypes', 'django.contrib.contenttypes'), ('django.contrib.sessions', 'django.contrib.sessions'), ('django.contrib.messages', 'django.contrib.messages'), ('django.contrib.staticfiles', 'django.contrib.staticfiles'), ('cart', 'cart'), ('loggers', 'loggers')], max_length=200),
        ),
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.PositiveIntegerField(verbose_name='Telegram User ID')),
                ('telegram_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]