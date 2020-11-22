# Generated by Django 2.2.12 on 2020-11-22 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0011_auto_20201122_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='source',
            field=models.CharField(choices=[('user_profile', 'user_profile'), ('jet', 'jet'), ('comments.apps.CommentsConfig', 'comments.apps.CommentsConfig'), ('notifications', 'notifications'), ('catalog', 'catalog'), ('django.contrib.admin', 'django.contrib.admin'), ('django.contrib.auth', 'django.contrib.auth'), ('django.contrib.contenttypes', 'django.contrib.contenttypes'), ('django.contrib.sessions', 'django.contrib.sessions'), ('django.contrib.messages', 'django.contrib.messages'), ('django.contrib.staticfiles', 'django.contrib.staticfiles'), ('rest_framework', 'rest_framework'), ('coupons', 'coupons'), ('cart', 'cart')], max_length=200),
        ),
    ]
