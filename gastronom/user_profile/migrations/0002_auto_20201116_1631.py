# Generated by Django 2.2.12 on 2020-11-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
<<<<<<< HEAD
            field=models.IntegerField(choices=[('Male', 'Male'), ('Female', 'Female'), ('not specified', 'not specified')]),
=======
            field=models.IntegerField(choices=[('Male', 'Male'), ('Female', 'Female'), ('not specified', 'not specified')], default='not specified'),
>>>>>>> b1a3fd9f09ad12453b0866621fc7c866f122410d
        ),
    ]