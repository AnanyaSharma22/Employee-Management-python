# Generated by Django 2.2 on 2020-04-22 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200422_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='dob',
            field=models.DateField(default=datetime.datetime(2020, 4, 22, 20, 18, 48, 692300), max_length=20, verbose_name='dob'),
        ),
        migrations.AddField(
            model_name='manager',
            name='dob',
            field=models.DateField(default=datetime.datetime(2020, 4, 22, 20, 18, 48, 680291), max_length=20, verbose_name='dob'),
        ),
    ]
