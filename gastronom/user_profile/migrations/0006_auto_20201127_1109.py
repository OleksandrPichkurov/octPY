# Generated by Django 2.2 on 2020-11-27 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20201127_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
