# Generated by Django 2.2.7 on 2020-01-08 16:29

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='NavigationMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NavigationMenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('menu_title_en', models.CharField(max_length=255)),
                ('menu_title_de', models.CharField(blank=True, max_length=255)),
                ('link_view', models.CharField(blank=True, choices=[('idea-list', 'ideaspace')], help_text='Creates a link to a non wagtail view (e.g ideaspace). Leave empty if you add subpages or a link page', max_length=100)),
                ('subpages', wagtail.core.fields.StreamField([('link', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock(required=True)), ('link_text_en', wagtail.core.blocks.CharBlock(required=True)), ('link_text_de', wagtail.core.blocks.CharBlock(required=False))]))], blank=True, help_text='These Links will be displayed in as a dropdown menu', null=True, verbose_name='Submenu')),
                ('link_page', models.ForeignKey(blank=True, help_text='Creates a link to a single wagtail page. Leave empty if you add subpages or a link view', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page')),
                ('parent', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='cms_snippets.NavigationMenu')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
