# Generated by Django 2.2.11 on 2020-03-31 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_settings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helppages',
            name='annual_theme_help_page',
        ),
        migrations.RemoveField(
            model_name='helppages',
            name='communication_camp_help_page',
        ),
        migrations.DeleteModel(
            name='CollaborationCampSettings',
        ),
    ]
