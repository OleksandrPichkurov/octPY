# Generated by Django 2.2 on 2020-12-02 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0008_auto_20201202_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewrating',
            name='disliked_review',
        ),
        migrations.RemoveField(
            model_name='reviewrating',
            name='liked_review',
        ),
        migrations.AddField(
            model_name='reviewrating',
            name='review_reting',
            field=models.ManyToManyField(blank=True, related_name='review_rating', to='comments.Review'),
        ),
    ]
