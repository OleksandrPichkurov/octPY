# Generated by Django 2.2 on 2020-11-27 09:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0021_auto_20201127_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcart',
            name='valid_date_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 25, 9, 11, 5, 821150, tzinfo=utc), verbose_name='Active to'),
        ),
    ]