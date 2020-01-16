from django_countries import Countries


class EuropeanCountries(Countries):
    only = ['BG', 'HR', 'CZ', 'GR', 'HU', 'IT',
            'PL', 'PT', 'RO', 'SK', 'SI', 'ES'
            ]
