# Generated by Django 2.2.10 on 2020-03-04 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civic_europe_ideas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='impact',
            field=models.TextField(help_text='We are looking for ideas that strengthen democracy and active citizenship in local communities. How does your idea enhance citizens’ engagement and participation? (max. 800 characters)', max_length=800, verbose_name='How does your idea strengthen democracy and active citizenship at a local and community level? Please refer to your described challenge.'),
        ),
    ]
