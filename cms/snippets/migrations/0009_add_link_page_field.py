# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 07:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_snippets', '0008_reintroduce_navigation_menu_without_multitable_inheritance'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationmenuitem',
            name='link_view',
            field=models.CharField(blank=True, choices=[('idea-sketch-list', 'ideaspace')], help_text='Creates a link to a non wagtail view (e.g ideaspace). Leave empty if you add subpages or a link page', max_length=100),
        ),
        migrations.AlterField(
            model_name='navigationmenuitem',
            name='link_page',
            field=models.ForeignKey(blank=True, help_text='Creates a link to a single wagtail page. Leave empty if you add subpages or a link view', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page'),
        ),
    ]
