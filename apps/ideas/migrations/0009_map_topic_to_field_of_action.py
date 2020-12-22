# Generated by Django 2.2.14 on 2020-12-22 14:04

from django.db import migrations

topic_to_field_of_action = {
    'DP': 'OT',
    'CE': 'OT',
    'CD': 'CD',
    'UP': 'CD',
    'SI': 'SI',
    'MI': 'SI',
    'ES': 'ES',
    'AC': 'AC'
}


def map_topic_to_field_of_action(apps, schema_editor):
    Idea = apps.get_model('civic_europe_ideas', 'Idea')
    for idea in Idea.objects.all():
        field_of_action = []
        for topic in idea.topics:
            field_of_action.append(topic_to_field_of_action[topic])
        #remove possible duplicates
        idea.field_of_action = list(set(field_of_action))
        idea.save()


def move_topic_other_to_field_of_action_other(apps, schema_editor):
    Idea = apps.get_model('civic_europe_ideas', 'Idea')
    for idea in Idea.objects.all():
        if idea.topics_other:
            idea.field_of_action_other = idea.topics_other[:50]
            idea.save()


class Migration(migrations.Migration):

    dependencies = [
        ('civic_europe_ideas', '0008_change_idea_section'),
    ]

    operations = [
        migrations.RunPython(map_topic_to_field_of_action),
        migrations.RunPython(move_topic_other_to_field_of_action_other),
    ]
