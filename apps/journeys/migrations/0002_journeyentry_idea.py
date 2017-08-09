# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0002_auto_20170809_1228'),
        ('advocate_europe_journeys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='journeyentry',
            name='idea',
            field=models.ForeignKey(default='no_idea', on_delete=django.db.models.deletion.CASCADE, to='advocate_europe_ideas.Idea'),
            preserve_default=False,
        ),
    ]
