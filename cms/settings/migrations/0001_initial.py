# Generated by Django 2.2.7 on 2020-01-08 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, help_text='Your Facebook page URL')),
                ('twitter', models.CharField(blank=True, help_text='Your twitter username, without the @', max_length=255)),
                ('flickr', models.URLField(blank=True, help_text='Your flickr page URL')),
                ('youtube', models.URLField(blank=True, help_text='Your YouTube channel or user account URL')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HelpPages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annual_theme_help_page', models.ForeignKey(blank=True, help_text='Please add a link to the page that explains the annual theme, impact and implementation.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='help_page_annual_theme', to='wagtailcore.Page')),
                ('communication_camp_help_page', models.ForeignKey(blank=True, help_text='Please add a link to the page that explains the idea challenge camp here.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='help_page_communication_camp', to='wagtailcore.Page', verbose_name='Idea Challenge Help Page')),
                ('selection_criteria', models.ForeignKey(blank=True, help_text='Please add a link to the page that explains the selection criteria here.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='help_page_selection_criteria', to='wagtailcore.Page')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
                ('terms_of_use_page', models.ForeignKey(blank=True, help_text='Please add a link to the page that explains the terms of condition here.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='help_page_terms_of_use_page', to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CollaborationCampSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Idea Challenge Camp Settings',
            },
        ),
    ]
