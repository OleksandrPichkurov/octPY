# Generated by Django 2.2 on 2020-11-27 08:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0020_auto_20201127_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcart',
            name='valid_date_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 25, 8, 53, 58, 485994, tzinfo=utc), verbose_name='Active to'),
        ),
    ]
