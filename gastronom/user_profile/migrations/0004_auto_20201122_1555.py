# Generated by Django 2.2.12 on 2020-11-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_auto_20201122_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.IntegerField(choices=[('Male', 'Male'), ('Female', 'Female'), ('not specified', 'not specified')], default='not specified'),
        ),
    ]
