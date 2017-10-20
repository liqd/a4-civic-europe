# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_users', '0009_user_get_notifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='get_notifications',
            field=models.BooleanField(default=True, verbose_name="my own ideas and ideas that I'm watching"),
        ),
    ]
