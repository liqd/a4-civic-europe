from django.utils.translation import gettext_lazy as _
from django_countries import Countries


class EuropeanCountries(Countries):
    only = ['BG', 'HR', 'GR', 'HU', 'IT', 'PL',
            'PT', 'RO', 'SK', 'SI', 'ES',
            ('CZ', _('Czech republic'))
            ]
