# Generated by Django 2.2.8 on 2020-01-16 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_home', '0004_remove_german'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='translated_title',
        ),
        migrations.RemoveField(
            model_name='simplepage',
            name='translated_title',
        ),
        migrations.RemoveField(
            model_name='structuredtextpage',
            name='translated_title',
        ),
    ]
