# Generated by Django 2.2 on 2020-12-11 13:09

import comments.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0009_auto_20201202_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewimage',
            name='raw_photo',
            field=models.ImageField(blank=True, null=True, upload_to=comments.models.review_photo_path),
        ),
    ]
