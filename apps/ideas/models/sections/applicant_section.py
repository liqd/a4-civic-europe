from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext as _
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField

from apps.ideas import fields as custom_fields
from apps.ideas.countries import EuropeanCountries

NON_PROFIT = 'NP'
CHARITY = 'CH'
PUBLIC_INSTITUTION = 'PI'
NON_PROFIT_PLANNED = 'PL'
OTHER = 'OT'

LEAD_ORGANISATION_STATUS_CHOICES = (
    (NON_PROFIT, _('I am applying on behalf of '
                   'a registered non-profit organization')),
    (CHARITY, _('I am applying on behalf of a registered '
                'organization with charitable purpose')),
    (PUBLIC_INSTITUTION, _('I am applying on behalf of a public institution')),
    (NON_PROFIT_PLANNED, _('Registration as a non-profit organization or '
                           'organization with charitable purpose is planned '
                           'or is already underway')),
    (OTHER, _('Other'))
)

CAPITAL_CITY = 'CC'
LARGE_URBAN_AREA = 'LA'
URBAN_AREA = 'UA'
TOWN = 'TW'
RURAL_AREA = 'RA'

LEAD_ORGANISATION_LOCATION_CHOICES = (
    (CAPITAL_CITY, _('Capital city')),
    (LARGE_URBAN_AREA, _('Large urban area (population of more than 500,000 '
                         'inhabitants)')),
    (URBAN_AREA, _('City/urban area (population of at least 50,000 '
                   'inhabitants and a density of >1,500 inhabitants '
                   'per km², most inhabitants have nonagricultural jobs, '
                   'there is good infrastructure such as housing, commercial '
                   'buildings, roads, bridges, and railways)')),
    (TOWN, _('Town (population of at least 5,000 inhabitants and a density of '
             'at least 300 inhabitants per km²)')),
    (RURAL_AREA, _('Village/rural area (population less than 5,000 '
                   'inhabitants, low population density, largely lacking '
                   'or poor infrastructure)')),
)

LEAD_ORGANISATION_NAME_HELP = _('If you do not yet have '
                                'a registered organization, '
                                'please write the name of '
                                'your initiative or planned '
                                'organization here. This section '
                                'will be published in the idea space.')
CLARIFICATION_LEGAL_STATUS_HELP = _('If you selected “Other,” please provide '
                                    'details about your current organization '
                                    'status. (Max. 200 characters.)')
LEAD_ORGANISATION_DETAILS_HELP = _('Please describe main goals, vision and '
                                   'activities of your organization. (Max. '
                                   '500 characters.)')
LEAD_ORGANISATION_WEBSITE_HELP = _('Please enter the website of your '
                                   'organization here. If you don’t have one, '
                                   'please enter your Facebook page or '
                                   'similar online presence. This section '
                                   'will be published in the idea space.')
LEAD_ORGANISATION_LOCATION_HELP = _('Please specify the type of the location '
                                    'to help us better understand the ideas. '
                                    'If your organization is based in '
                                    'more than one location, you can choose '
                                    'more options. The numbers here are more '
                                    'for orientation, you don’t have to look '
                                    'up the exact numbers; a rough estimate '
                                    'will suffice.')


class ApplicantSection(models.Model):
    first_name = models.CharField(
        max_length=250,
    )
    last_name = models.CharField(
        max_length=250
    )
    lead_organisation_name = models.CharField(
        max_length=300,
        blank=True,
        verbose_name=_('Lead organization name'),
        help_text=LEAD_ORGANISATION_NAME_HELP
    )
    lead_organisation_status = models.CharField(
        max_length=255,
        verbose_name=_('Lead organization status'),
        choices=LEAD_ORGANISATION_STATUS_CHOICES
    )
    clarification_legal_status = models.TextField(
        max_length=200,
        blank=True,
        verbose_name=_('Clarification legal status'),
        help_text=CLARIFICATION_LEGAL_STATUS_HELP
    )
    lead_organisation_details = models.TextField(
        max_length=500,
        blank=True,
        verbose_name=_('Lead organization details'),
        help_text=LEAD_ORGANISATION_DETAILS_HELP
    )
    lead_organisation_website = models.URLField(
        max_length=500,
        blank=True,
        verbose_name=_('Lead organization online presence '
                       '(website or social media presence)'),
        help_text=LEAD_ORGANISATION_WEBSITE_HELP
    )
    lead_organisation_country = CountryField(
        blank=True,
        countries=EuropeanCountries,
        verbose_name=_('Lead organization country')
    )
    lead_organisation_location_name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name=_('Lead organization location name')
    )
    lead_organisation_location = MultiSelectField(
        max_length=255,
        blank=True,
        choices=LEAD_ORGANISATION_LOCATION_CHOICES,
        verbose_name=_('Location'),
        help_text=LEAD_ORGANISATION_LOCATION_HELP
    )
    contact_email = models.EmailField(
        blank=True,
        verbose_name=_('Lead organization email')
    )
    year_of_registration = custom_fields.CustomIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(2050),
            MinValueValidator(0)
        ]
    )

    class Meta:
        abstract = True
