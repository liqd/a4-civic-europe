# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-26 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civic_europe_ideas', '0020_wording_add_and_remove_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='network',
            field=models.TextField(help_text='The Advocate Europe network includes all previous winning projects, jury members, the online community, the partner organisations Stiftung Mercator, MitOst e.V. and Liquid Democracy e.V. and the Advocate Europe team. Winning projects meet at least one time per year in network meetings. Tell us about your expectations. Think about your skills, resources, networks and partners when describing what you could offer and what you would like to take away. (max. 800 characters)', max_length=800, verbose_name='How will you contribute to and benefit from the Advocate Europe network?'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='selection_apart',
            field=models.TextField(help_text='What is surprising or unconventional about your idea? What is special about it? (max. 800 characters)', max_length=800, verbose_name='What makes your idea stand apart?'),
        ),
    ]
