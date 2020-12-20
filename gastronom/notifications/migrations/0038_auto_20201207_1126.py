# Generated by Django 2.2 on 2020-12-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0037_auto_20201207_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='source',
            field=models.CharField(choices=[('rest_framework', 'rest_framework'), ('django_filters', 'django_filters'), ('user_profile', 'user_profile'), ('jet', 'jet'), ('comments.apps.CommentsConfig', 'comments.apps.CommentsConfig'), ('notifications', 'notifications'), ('catalog', 'catalog'), ('product.apps.ProductConfig', 'product.apps.ProductConfig'), ('cart', 'cart'), ('django.contrib.admin', 'django.contrib.admin'), ('django.contrib.auth', 'django.contrib.auth'), ('django.contrib.contenttypes', 'django.contrib.contenttypes'), ('django.contrib.sessions', 'django.contrib.sessions'), ('django.contrib.messages', 'django.contrib.messages'), ('django.contrib.staticfiles', 'django.contrib.staticfiles'), ('discount', 'discount')], max_length=200),
        ),
    ]
