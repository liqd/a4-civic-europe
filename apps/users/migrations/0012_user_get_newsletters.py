# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-18 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civic_europe_users', '0011_change_wording_avatar_helptext'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='get_newsletters',
            field=models.BooleanField(default=False, help_text='Designates whether you want to receive newsletters. Unselect if you do not want to receive newsletters.', verbose_name='Send me newsletters'),
        ),
    ]
