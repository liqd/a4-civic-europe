from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext as _

TOTAL_BUDGET_HELP = _('Please indicate your overall budget. '
                      'The total budget may (but does not have to) '
                      'include the applicant’s own contribution '
                      'and/or external sources of funding. This '
                      'section will be published in the idea space.')

BUDGET_REQUESTED_HELP = _('Funding requested from Civic Europe '
                          'can range from 1 to 50,000 EUR. Depending '
                          'on your planning, the amount entered here '
                          'can be the same as the “total budget” '
                          'figure entered above. This section will be '
                          'published in the idea space.')

MAJOR_EXPENSES_HELP = _('What are the major expenses you foresee for the '
                        'implementation of your idea? Please share a rough '
                        'estimate by cost category (e.g. office expenses '
                        '1000 EUR, travel and accommodation costs 3000 EUR, '
                        'public relations 2000 EUR, personnel costs etc.) '
                        'This section will be published in the idea space.')

DURATION_HELP = _('How many months will it take to implement your idea?')


class FinancesSection(models.Model):
    total_budget = models.IntegerField(
        verbose_name=_('Total budget'),
        help_text=TOTAL_BUDGET_HELP,
        validators=[
            MinValueValidator(0)
        ]
    )
    budget_requested = models.IntegerField(
        verbose_name=_('Funding requested from Civic Europe'),
        help_text=BUDGET_REQUESTED_HELP,
        validators=[
            MaxValueValidator(50000),
            MinValueValidator(0)
        ]
    )
    major_expenses = models.TextField(
        max_length=500,
        verbose_name=_('Major expenses'),
        help_text=MAJOR_EXPENSES_HELP
    )
    duration = models.IntegerField(
        verbose_name=_('Duration of idea (number of months)'),
        help_text=DURATION_HELP
    )

    class Meta:
        abstract = True
