# Generated by Django 2.2 on 2020-11-27 07:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0014_auto_20201126_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcart',
            name='valid_date_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 25, 7, 50, 47, 794354, tzinfo=utc), verbose_name='Active to'),
        ),
    ]
