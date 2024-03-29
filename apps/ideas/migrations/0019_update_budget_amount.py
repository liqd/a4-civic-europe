# Generated by Django 2.2.17 on 2021-02-08 10:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civic_europe_ideas', '0018_update_detail_role_formfields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='budget_requested',
            field=models.IntegerField(help_text='Funding requested from Civic Europe can range from 1 to 35000 EUR. Depending on your planning, the amount entered here can be the same as the “total budget” figure entered above. This section will be published in the idea space.', validators=[django.core.validators.MaxValueValidator(35000), django.core.validators.MinValueValidator(0)], verbose_name='Funding requested from Civic Europe'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='total_budget',
            field=models.IntegerField(help_text='Please indicate your overall budget. The total budget may (but does not have to) include the applicant’s own contribution and/or external sources of funding. Please only enter whole numbers, no decimal signs like points, commas or spaces. This section will be published in the idea space.', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Total budget'),
        ),
    ]
