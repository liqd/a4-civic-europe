# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-14 13:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('civic_europe_ideas', '0017_change_some_helptexts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ideasketch',
            old_name='collaboration_camp_represent',
            new_name='idea_challenge_camp_represent',
        ),
        migrations.RenameField(
            model_name='ideasketcharchived',
            old_name='collaboration_camp_represent',
            new_name='idea_challenge_camp_represent',
        ),
        migrations.RenameField(
            model_name='ideasketch',
            old_name='collaboration_camp_benefit',
            new_name='idea_challenge_camp_benefit',
        ),
        migrations.RenameField(
            model_name='ideasketcharchived',
            old_name='collaboration_camp_benefit',
            new_name='idea_challenge_camp_benefit',
        ),
    ]
