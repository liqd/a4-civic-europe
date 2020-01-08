# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 09:34
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civic_europe_users', '0003_increase_username_length_to_75'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 60 characters or fewer. Letters, digits, spaces and @/./+/-/_ only.', max_length=75, unique=True, validators=[django.core.validators.RegexValidator('^[\\w]+[ \\w.@+\\-]*$', 'Enter a valid username. This value may contain only letters, digits, spaces and @/./+/-/_ characters. It must start with a digit or a letter.', 'invalid')], verbose_name='username'),
        ),
    ]
