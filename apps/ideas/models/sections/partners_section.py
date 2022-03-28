from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField

from apps.ideas.countries import EuropeanCountries

from .applicant_section import LEAD_ORGANISATION_LOCATION_CHOICES

PARTNERS_NAME_LABEL = _('Organization Name')
PARTNERS_NAME_HELP = _('This section will be published in the idea space.')
PARTNERS_WEBSITE_LABEL = _('Online presence (website or social media '
                           'presence)')
PARTNERS_WEBSITE_HELP = _('Please enter the website of your partner here. If '
                          'they don’t have one, please enter their Facebook '
                          'page or similar online presence. This section will '
                          'be published in the idea space.')
PARTNERS_COUNTRY_LABEL = _('country')
PARTNERS_LOCATION_NAME_LABEL = _('Location Name')
PARTNERS_LOCATION_HELP = _('Please specify the type of the location to help '
                           'us better understand the ideas. If your partner '
                           'organization is based in more than one location, '
                           'you can choose more options. The numbers here '
                           'are more for orientation, you don’t have to look '
                           'up the exact numbers; a rough estimate will '
                           'suffice.')
PARTNERS_DETAILS_LABEL = _('Partner organization details')
PARTNERS_DETAILS_HELP = _('Please describe main goals, vision and activities '
                          'of the organization. Please also mention the '
                          'organization status (NGO, public institution, '
                          'enterprise, etc.). Any organization status is '
                          'possible for partners. (Max. 400 characters.)')
PARTNERS_ROLE_LABEL = _('Please describe the role of your partner in your '
                        'project')
PARTNERS_ROLE_HELP = _('Why did you choose this partner and how will your '
                       'partner support you? (Max. 400 characters.)')
PARTNERS_MORE_INFO_HELP = _('Please use this field if you have more than '
                            'three partner organizations. Please also let '
                            'us know about planned partnerships. This '
                            'section will be published in the idea space. '
                            '(Max. 200 characters.)')
CO_WORKERS_LABEL = _('Please add your team members here.')
CO_WORKERS_HELP = _('Here you can insert the email addresses of up to four '
                    'team members, separated with commas. They will receive '
                    'an email inviting them to register on the Civic Europe '
                    'website. After registering they will appear with their '
                    'user name on your idea page and will be able to edit '
                    'your idea. The email addresses will not be published in '
                    'the idea space. Please note: You can only add your team '
                    'members until the application period ends. Furthermore, '
                    'only you and the team members you add will be able to '
                    'later take part in the Community Award vote.')


class PartnersSection(models.Model):
    partner_organisation_1_name = models.CharField(
        max_length=300,
        blank=True,
        verbose_name=PARTNERS_NAME_LABEL,
        help_text=PARTNERS_NAME_HELP
    )
    partner_organisation_1_website = models.URLField(
        max_length=500,
        blank=True,
        verbose_name=PARTNERS_WEBSITE_LABEL,
        help_text=PARTNERS_WEBSITE_HELP
    )
    partner_organisation_1_country = CountryField(
        blank=True,
        verbose_name=PARTNERS_COUNTRY_LABEL,
        countries=EuropeanCountries
    )
    partner_organisation_1_location_name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name=PARTNERS_LOCATION_NAME_LABEL
    )
    partner_organisation_1_location = MultiSelectField(
        max_length=255,
        blank=True,
        choices=LEAD_ORGANISATION_LOCATION_CHOICES,
        verbose_name=_('Location'),
        help_text=PARTNERS_LOCATION_HELP
    )
    partner_organisation_1_details = models.TextField(
        max_length=400,
        blank=True,
        verbose_name=PARTNERS_DETAILS_LABEL,
        help_text=PARTNERS_DETAILS_HELP
    )
    partner_organisation_1_role = models.TextField(
        max_length=400,
        blank=True,
        verbose_name=PARTNERS_ROLE_LABEL,
        help_text=PARTNERS_ROLE_HELP
    )
    partner_organisation_2_name = models.CharField(
        max_length=300,
        blank=True,
        verbose_name=PARTNERS_NAME_LABEL,
        help_text=PARTNERS_NAME_HELP
    )
    partner_organisation_2_website = models.URLField(
        max_length=500,
        blank=True,
        verbose_name=PARTNERS_WEBSITE_LABEL,
        help_text=PARTNERS_WEBSITE_HELP
    )
    partner_organisation_2_country = CountryField(
        blank=True,
        verbose_name=PARTNERS_COUNTRY_LABEL,
        countries=EuropeanCountries
    )
    partner_organisation_2_location_name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name=PARTNERS_LOCATION_NAME_LABEL
    )
    partner_organisation_2_location = MultiSelectField(
        max_length=255,
        blank=True,
        choices=LEAD_ORGANISATION_LOCATION_CHOICES,
        verbose_name=_('Location'),
        help_text=PARTNERS_LOCATION_HELP
    )
    partner_organisation_2_details = models.TextField(
        max_length=400,
        blank=True,
        verbose_name=PARTNERS_DETAILS_LABEL,
        help_text=PARTNERS_DETAILS_HELP
    )
    partner_organisation_2_role = models.TextField(
        max_length=400,
        blank=True,
        verbose_name=PARTNERS_ROLE_LABEL,
        help_text=PARTNERS_ROLE_HELP
    )
    partner_organisation_3_name = models.CharField(
        max_length=300,
        blank=True,
        verbose_name=PARTNERS_NAME_LABEL,
        help_text=PARTNERS_NAME_HELP
    )
    partner_organisation_3_website = models.URLField(
        max_length=500,
        blank=True,
        verbose_name=PARTNERS_WEBSITE_LABEL,
        help_text=PARTNERS_WEBSITE_HELP
    )
    partner_organisation_3_country = CountryField(
        blank=True,
        verbose_name=PARTNERS_COUNTRY_LABEL,
        countries=EuropeanCountries
    )
    partner_organisation_3_location_name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name=PARTNERS_LOCATION_NAME_LABEL
    )
    partner_organisation_3_location = MultiSelectField(
        max_length=255,
        blank=True,
        choices=LEAD_ORGANISATION_LOCATION_CHOICES,
        verbose_name=_('Location'),
        help_text=PARTNERS_LOCATION_HELP
    )
    partner_organisation_3_details = models.TextField(
        max_length=400,
        blank=True,
        verbose_name=PARTNERS_DETAILS_LABEL,
        help_text=PARTNERS_DETAILS_HELP
    )
    partner_organisation_3_role = models.TextField(
        max_length=400,
        blank=True,
        verbose_name=PARTNERS_ROLE_LABEL,
        help_text=PARTNERS_ROLE_HELP
    )
    partners_more_info = models.TextField(
        blank=True,
        max_length=200,
        verbose_name='More information',
        help_text=PARTNERS_MORE_INFO_HELP
    )
    co_workers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='%(class)s_co_workers',
        blank=True,
        verbose_name=CO_WORKERS_LABEL,
        help_text=CO_WORKERS_HELP)

    class Meta:
        abstract = True
