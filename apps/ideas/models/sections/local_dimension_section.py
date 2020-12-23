from django.db import models
from django.utils.translation import ugettext as _
from multiselectfield import MultiSelectField

from .applicant_section import LEAD_ORGANISATION_LOCATION_CHOICES

MIXED_LOCATION = 'ML'
LOCATION_DETAILS_CHOICES = LEAD_ORGANISATION_LOCATION_CHOICES + \
                           ((MIXED_LOCATION, _('Mixed location (if your '
                                               'project will take place '
                                               'in several locations)')),)

LOCATION_HELP = _('Please name city, country and/or region (max. 100 '
                  'characters). For instance: “Teleorman, south Romania.” ')

LOCATION_DETAILS_HELP = _('Please specify the type of the location. We are '
                          'aware that national definitions of urban and '
                          'rural areas differ significantly and places with '
                          'the same number of inhabitants can be perceived '
                          'in some countries as urban and in others as '
                          'rural. This question merely helps us to better '
                          'categorize the prospective locations.')

CHALLENGE_HELP = _('Tell us more about the region your project idea is based '
                   'in and what challenges it faces regarding democracy and '
                   'societal cohesion. What problem(s) are you trying to '
                   'solve? (max. 800 characters)')

IMPACT_HELP = _('We are looking for ideas that strengthen democracy and '
                'active citizenship in local communities. How does your idea '
                'enhance citizens’ engagement and participation? '
                '(max. 800 characters)')

TARGET_GROUP_HELP = _('We are looking for ideas that try to engage different '
                      'perspectives from all local voices of the communities '
                      'including those who feel excluded. Please '
                      'describe what target groups, beneficiaries '
                      'or audiences will be affected by your idea. '
                      'How will you include the whole '
                      'range of opinions on the issue? Try to add some key '
                      'figures about the groups of people you are going to '
                      'be working with. (max. 800 characters)')

LOCAL_EMBEDDING_HELP = _('How will you be working with local '
                         'supporters, partners and/or allies? '
                         'Please refer to established networks you '
                         'might have or want to establish and/or '
                         'possible institutional supporters '
                         '(administrational bodies, organisations). '
                         '(max. 800 characters)')

UNIQUENESS_HELP = _('Please describe what niche your initiative '
                    'is filling in the specific region and context '
                    'you are describing above. (max. 800 characters)')


class LocalDimensionSection(models.Model):
    location = models.TextField(
        max_length=100,
        verbose_name=_('Where will your project take place?'),
        help_text=LOCATION_HELP
    )
    location_details = MultiSelectField(
        max_length=255,
        choices=LOCATION_DETAILS_CHOICES,
        verbose_name=_('Location'),
        help_text=LOCATION_DETAILS_HELP,
        max_choices=1
    )
    challenge = models.TextField(
        max_length=800,
        verbose_name=_('What is the specific societal challenge '
                       'faced by the region in which your project '
                       'idea is based?'),
        help_text=CHALLENGE_HELP
    )
    impact = models.TextField(
        max_length=800,
        verbose_name=_('How does your idea strengthen democracy '
                       'and active citizenship at a local and '
                       'community level? Please refer to your '
                       'described challenge.'),
        help_text=IMPACT_HELP
    )
    target_group = models.TextField(
        max_length=800,
        verbose_name=_('Who are you doing it for? '),
        help_text=TARGET_GROUP_HELP
    )
    local_embedding = models.TextField(
        max_length=800,
        verbose_name=_('How is your idea embedded locally? '),
        help_text=LOCAL_EMBEDDING_HELP
    )
    uniqueness = models.TextField(
        max_length=800,
        verbose_name=_('What makes your idea stand apart in '
                       'its local and regional dimension? '),
        help_text=UNIQUENESS_HELP
    )

    class Meta:
        abstract = True
