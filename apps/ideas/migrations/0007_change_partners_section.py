# Generated by Django 2.2.14 on 2020-12-18 16:01

from django.conf import settings
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('civic_europe_ideas', '0006_update_lead_organisation_status_to_new_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='partner_organisation_1_details',
            field=models.CharField(blank=True, help_text='Please describe main goals, vision and activities of the organisation. Please also mention the organisation status (NGO, public institution, enterprise, etc.). Any organisation status is possible for partners. (max. 400 characters)', max_length=400, verbose_name='Partner organisation details'),
        ),
        migrations.AddField(
            model_name='idea',
            name='partner_organisation_1_location',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('CC', 'Capital city'), ('LA', 'Large urban area (population of more than 500,000 inhabitants)'), ('UA', 'City/urban area (population of at least 50,000 inhabitants and a density of >1,500 inhabitants per km2, most inhabitants have nonagricultural jobs, there is good infrastructure such as housing, commercial buildings, roads, bridges, and railways)'), ('TW', 'Town (population of at least 5,000 inhabitants and a density of at least 300 inhabitants per km2)'), ('RA', 'Village/rural area (population less than 5,000 inhabitants, low population density, largely lacking or poor infrastructure)')], help_text='Please specify the type of the location to help us better understand the ideas. If your partner organisation is based in more than one location, you can choose more options. The numbers here are more for orientation, you don’t have to look up the exact numbers; a rough estimate will suffice.', max_length=255, verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='idea',
            name='partner_organisation_1_location_name',
            field=models.CharField(blank=True, max_length=250, verbose_name='Location Name'),
        ),
        migrations.AddField(
            model_name='idea',
            name='partner_organisation_1_role',
            field=models.CharField(blank=True, help_text='Why did you choose this partner and how will your partner support you? (max. 400 characters)', max_length=400, verbose_name='Please describe the role of your partner in your project'),
        ),
        migrations.AddField(
            model_name='idea',
            name='partner_organisation_2_details',
            field=models.CharField(blank=True, help_text='Please describe main goals, vision and activities of the organisation. Please also mention the organisation status (NGO, public institution, enterprise, etc.). Any organisation status is possible for partners. (max. 400 characters)', max_length=400, verbose_name='Partner organisation details'),
        ),
        migrations.AddField(
            model_name='idea',
            name='partner_organisation_2_location',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('CC', 'Capital city'), ('LA', 'Large urban area (population of more than 500,000 inhabitants)'), ('UA', 'City/urban area (population of at least 50,000 inhabitants and a density of >1,500 inhabitants per km2, most inhabitants have nonagricultural jobs, there is good infrastructure such as housing, commercial buildings, roads, bridges, and railways)'), ('TW', 'Town (population of at least 5,000 inhabitants and a density of at least 300 inhabitants per km2)'), ('RA', 'Village/rural area (population less than 5,000 inhabitants, low population density, largely lacking or poor infrastructure)')], help_text='Please specify the type of the location to help us better understand the ideas. If your partner organisation is based in more than one location, you can choose more options. The numbers here are more for orientation, you don’t have to look up the exact numbers; a rough estimate will suffice.', max_length=255, verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='idea',
            name='partner_organisation_2_location_name',
            field=models.CharField(blank=True, max_length=250, verbose_name='Location Name'),
        ),
        migrations.AddField(
            model_name='idea',
            name='partner_organisation_2_role',
            field=models.CharField(blank=True, help_text='Why did you choose this partner and how will your partner support you? (max. 400 characters)', max_length=400, verbose_name='Please describe the role of your partner in your project'),
        ),
        migrations.AddField(
            model_name='idea',
            name='partner_organisation_3_details',
            field=models.CharField(blank=True, help_text='Please describe main goals, vision and activities of the organisation. Please also mention the organisation status (NGO, public institution, enterprise, etc.). Any organisation status is possible for partners. (max. 400 characters)', max_length=400, verbose_name='Partner organisation details'),
        ),
        migrations.AddField(
            model_name='idea',
            name='partner_organisation_3_location',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('CC', 'Capital city'), ('LA', 'Large urban area (population of more than 500,000 inhabitants)'), ('UA', 'City/urban area (population of at least 50,000 inhabitants and a density of >1,500 inhabitants per km2, most inhabitants have nonagricultural jobs, there is good infrastructure such as housing, commercial buildings, roads, bridges, and railways)'), ('TW', 'Town (population of at least 5,000 inhabitants and a density of at least 300 inhabitants per km2)'), ('RA', 'Village/rural area (population less than 5,000 inhabitants, low population density, largely lacking or poor infrastructure)')], help_text='Please specify the type of the location to help us better understand the ideas. If your partner organisation is based in more than one location, you can choose more options. The numbers here are more for orientation, you don’t have to look up the exact numbers; a rough estimate will suffice.', max_length=255, verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='idea',
            name='partner_organisation_3_location_name',
            field=models.CharField(blank=True, max_length=250, verbose_name='Location Name'),
        ),
        migrations.AddField(
            model_name='idea',
            name='partner_organisation_3_role',
            field=models.CharField(blank=True, help_text='Why did you choose this partner and how will your partner support you? (max. 400 characters)', max_length=400, verbose_name='Please describe the role of your partner in your project'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='co_workers',
            field=models.ManyToManyField(blank=True, help_text='Here you can insert the email addresses of up to four team members, separated with commas. They will receive an email inviting them to register on the Civic Europe website. After registering they will appear with their user name on your idea page and will be able to edit your idea. The email addresses will not be published in the idea space. Please note: You can only add your team members until the application period ends. Furthermore, only you and the team members you add will be able to later take part in the Community Award vote.', related_name='idea_co_workers', to=settings.AUTH_USER_MODEL, verbose_name='Please add your team members here.'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='partner_organisation_1_website',
            field=models.URLField(blank=True, max_length=500, verbose_name='Online presence (website or social media presence)'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='partner_organisation_2_website',
            field=models.URLField(blank=True, max_length=500, verbose_name='Online presence (website or social media presence)'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='partner_organisation_3_website',
            field=models.URLField(blank=True, max_length=500, verbose_name='Online presence (website or social media presence)'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='partners_more_info',
            field=models.TextField(blank=True, help_text='Please use this field if you have more than three partner organisations. Please also let us know about planned partnerships. (max. 200 characters)', max_length=200, verbose_name='More information'),
        ),
    ]
