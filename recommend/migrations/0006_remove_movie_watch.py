# Generated by Django 3.0.6 on 2022-06-09 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0005_auto_20200609_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='watch',
        ),
    ]
