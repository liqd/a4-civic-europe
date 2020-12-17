# Generated by Django 2.2.14 on 2020-12-15 15:51

from django.db import migrations


def update_lead_organisation_status(apps, schema_editor):
    Idea = apps.get_model('civic_europe_ideas', 'Idea')
    for idea in Idea.objects.all():
        if idea.lead_organisation_status == 'HN':
            idea.lead_organisation_status = 'OT'
            idea.save()


class Migration(migrations.Migration):

    dependencies = [
        ('civic_europe_ideas', '0005_change_applicant_section'),
    ]

    operations = [
        migrations.RunPython(update_lead_organisation_status),
    ]
