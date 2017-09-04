# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 10:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advocate_europe_ideas', '0009_move_jurystatement'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False, null=True)),
                ('enabled', models.BooleanField(default=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('followable', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='advocate_europe_ideas.Idea')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='ideafollow',
            unique_together=set([('followable', 'creator')]),
        ),
    ]
