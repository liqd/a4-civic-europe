# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 09:32
from __future__ import unicode_literals

import apps.ideas.countries
from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0005_increase_length_of_url_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='organisation_country',
            field=django_countries.fields.CountryField(blank=True, countries=apps.ideas.countries.EuropeanCountries, max_length=2),
        ),
        migrations.AlterField(
            model_name='idea',
            name='partner_organisation_1_country',
            field=django_countries.fields.CountryField(blank=True, countries=apps.ideas.countries.EuropeanCountries, max_length=2, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='partner_organisation_2_country',
            field=django_countries.fields.CountryField(blank=True, countries=apps.ideas.countries.EuropeanCountries, max_length=2, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='partner_organisation_3_country',
            field=django_countries.fields.CountryField(blank=True, countries=apps.ideas.countries.EuropeanCountries, max_length=2, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='ideasketcharchived',
            name='organisation_country',
            field=django_countries.fields.CountryField(blank=True, countries=apps.ideas.countries.EuropeanCountries, max_length=2),
        ),
        migrations.AlterField(
            model_name='ideasketcharchived',
            name='partner_organisation_1_country',
            field=django_countries.fields.CountryField(blank=True, countries=apps.ideas.countries.EuropeanCountries, max_length=2, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='ideasketcharchived',
            name='partner_organisation_2_country',
            field=django_countries.fields.CountryField(blank=True, countries=apps.ideas.countries.EuropeanCountries, max_length=2, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='ideasketcharchived',
            name='partner_organisation_3_country',
            field=django_countries.fields.CountryField(blank=True, countries=apps.ideas.countries.EuropeanCountries, max_length=2, verbose_name='country'),
        ),
    ]
