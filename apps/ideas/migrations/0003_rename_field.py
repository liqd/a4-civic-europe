# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 15:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0002_alter_help_texts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idea',
            old_name='visit_camp',
            new_name='is_on_shortlist',
        ),
    ]
