# Generated by Django 2.2 on 2020-11-26 15:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0005_auto_20201126_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcart',
            name='valid_date_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 24, 15, 24, 3, 495828, tzinfo=utc), verbose_name='Active to'),
        ),
    ]