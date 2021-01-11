# Generated by Django 2.2 on 2020-12-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_auto_20201209_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmedia',
            name='large_image',
            field=models.ImageField(editable=False, null=True, upload_to='products/%Y/%m/%d/large/'),
        ),
        migrations.AddField(
            model_name='productmedia',
            name='medium_image',
            field=models.ImageField(editable=False, null=True, upload_to='products/%Y/%m/%d/medium/'),
        ),
        migrations.AddField(
            model_name='productmedia',
            name='medium_large_image',
            field=models.ImageField(editable=False, null=True, upload_to='products/%Y/%m/%d/medium_large/'),
        ),
        migrations.AlterField(
            model_name='productmedia',
            name='thumbnail_image',
            field=models.ImageField(editable=False, null=True, upload_to='products/%Y/%m/%d/thumbnail/'),
        ),
    ]