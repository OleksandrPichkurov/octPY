# Generated by Django 2.2 on 2020-11-26 15:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0002_auto_20201126_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcart',
            name='valid_date_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 24, 15, 1, 50, 601617, tzinfo=utc), verbose_name='Active to'),
        ),
    ]
