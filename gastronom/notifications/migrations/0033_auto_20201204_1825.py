# Generated by Django 2.2 on 2020-12-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0032_auto_20201204_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramincomemessage',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date'),
        ),
    ]
