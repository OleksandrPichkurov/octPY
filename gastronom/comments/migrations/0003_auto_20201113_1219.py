# Generated by Django 2.2 on 2020-11-13 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0002_auto_20201111_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImageReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_photo', models.ImageField(blank=True, null=True, upload_to='reviews/')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('reply_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='comments.Review', verbose_name='reply_review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='review_user')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='ReviewLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField(default=0)),
                ('reviews', models.ManyToManyField(to='comments.Review')),
            ],
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='reply_to',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usefulkarma',
            name='reviews',
        ),
        migrations.DeleteModel(
            name='CommentGalleryItem',
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
        migrations.DeleteModel(
            name='UsefulKarma',
        ),
        migrations.AddField(
            model_name='galleryimagereview',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.Review'),
        ),
    ]