# Generated by Django 3.0.6 on 2022-06-09 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0010_remove_movie_watch'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='watch',
            field=models.BooleanField(default=False),
        ),
    ]
