from django.db import models
from django.utils.translation import ugettext as _
from django_countries.fields import CountryField

from apps.ideas.countries import EuropeanCountries

LEAD_ORGANISATION_NAME_HELP = _('If you do not yet have '
                                'a registered organisation, '
                                'please write the name of '
                                'your initiative or planned '
                                'organisation here.')

NON_PROFIT = 'NP'
NON_PROFIT_PLANNED = 'PL'
HELP_NEEDED = 'HN'
OTHER = 'OT'

LEAD_ORGANISATION_STATUS_CHOICES = (
    (NON_PROFIT, _('I am applying on behalf of '
                   'a registered non-profit organisation, '
                   'e.g. NGO')),
    (NON_PROFIT_PLANNED, _('Registration as a non-profit '
                           'organisation is planned or is '
                           'already underway')),
    (HELP_NEEDED, _('I have a really good idea, '
                    'but will need help to register '
                    'a non-profit organisation')),
    (OTHER, _('Other'))
)

LEAD_ORGANISATION_DETAILS_HELP = _('Please provide details about '
                                   'your current status, especially '
                                   'if you selected "Other" (max. 200 '
                                   'characters)')


class ApplicantSection(models.Model):
    first_name = models.CharField(
        max_length=250
    )
    last_name = models.CharField(
        max_length=250
    )
    lead_organisation_name = models.CharField(
        max_length=300,
        blank=True,
        verbose_name=_('Lead organisation name'),
        help_text=LEAD_ORGANISATION_NAME_HELP
    )
    lead_organisation_status = models.CharField(
        max_length=255,
        verbose_name=_('Lead organisation status'),
        choices=LEAD_ORGANISATION_STATUS_CHOICES
    )
    lead_organisation_details = models.TextField(
        max_length=200,
        blank=True,
        verbose_name=_('Lead organisation details'),
        help_text=LEAD_ORGANISATION_DETAILS_HELP
    )
    lead_organisation_website = models.URLField(
        max_length=500,
        blank=True
    )
    lead_organisation_country = CountryField(
        blank=True,
        countries=EuropeanCountries
    )
    lead_organisation_city = models.CharField(
        max_length=250,
        blank=True
    )
    contact_email = models.EmailField(
        blank=True,
        verbose_name=_('Lead organisation email')
    )
    year_of_registration = models.IntegerField(
        blank=True,
        null=True
    )

    class Meta:
        abstract = True
