# Generated by Django 2.2 on 2020-11-13 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=1, verbose_name='Quantity'),
        ),
    ]
