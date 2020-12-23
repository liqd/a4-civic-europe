from django.db import models
from django.utils.translation import ugettext as _

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

LOCATION_DETAILS_MIXED_HELP = _('(max. 100 characters)')

COHESION_HELP = _('Civic cohesion is defined as the ability, knowledge and '
                  'willingness of individuals to cooperate with each other '
                  'in order to prosper, grow and learn as a community in a '
                  'changing world. Is this not the case in this region and '
                  'why? Do community members lack an understanding that '
                  'citizens can act and contribute to positive change in '
                  'their community and why? Does the civic infrastructure '
                  'include a striving civil society sector, informal groups, '
                  'access to decision and policymaking, community centers, '
                  'libraries, museums, etc.? Please specify. '
                  '(max. 800 characters)')

CHALLENGE_HELP = _('Please be concise and refer only to the challenge(s) '
                   'that your project will address. If possible, link this '
                   'answer to your previous answer. (max. 800 characters) ')

IMPACT_HELP = _('We are looking for ideas that strengthen democracy and '
                'active citizenship in local communities. How does your idea '
                'enhance citizens’ engagement and participation? '
                '(max. 800 characters)')

TARGET_GROUP_HELP = _('Please describe the key target groups that you want '
                      'to reach with your project. Try to add some key '
                      'figures about the groups you will be working with. '
                      '(max. 800 characters)')

LOCAL_EMBEDDING_HELP = _('Networks, allies, public bodies or others you '
                         'want to include in order to implement your '
                         'project successfully. (max. 800 characters)')

UNIQUENESS_HELP = _('Please describe what niche your initiative '
                    'is filling in the specific region and context '
                    'you are describing above. (max. 800 characters)')

PERSPECTIVE_AND_DIALOG_HELP = _('We are looking for ideas that try to build '
                                'bridges between differently-minded people. '
                                'How will you invite people who have '
                                'different opinions or different perspectives '
                                'to engage? How will you ensure that '
                                'marginalized voices or perspectives can '
                                'be heard? (max. 800 characters)')


class LocalDimensionSection(models.Model):
    location = models.CharField(
        max_length=100,
        verbose_name=_('Where will your project take place?'),
        help_text=LOCATION_HELP
    )
    location_details = models.CharField(
        default=MIXED_LOCATION,
        max_length=2,
        choices=LOCATION_DETAILS_CHOICES,
        verbose_name=_('Location'),
        help_text=LOCATION_DETAILS_HELP
    )
    location_details_mixed = models.CharField(
        blank=True,
        max_length=100,
        verbose_name=_('If you chose “Mixed location”, please specify '
                       'them briefly here.'),
        help_text=LOCATION_DETAILS_MIXED_HELP
    )
    cohesion = models.TextField(
        default=_('This question did not exist when this idea was created'),
        max_length=800,
        verbose_name=_('Why is this region or community lacking civic '
                       'cohesion and engagement?'),
        help_text=COHESION_HELP
    )
    challenge = models.TextField(
        max_length=800,
        verbose_name=_('What is the specific societal challenge faced by '
                       'this region that you aim to tackle with '
                       'your project?'),
        help_text=CHALLENGE_HELP
    )
    impact = models.TextField(
        blank=True,
        max_length=800,
        verbose_name=_('How does your idea strengthen democracy '
                       'and active citizenship at a local and '
                       'community level? Please refer to your '
                       'described challenge. '),
        help_text=IMPACT_HELP
    )
    target_group = models.TextField(
        max_length=800,
        verbose_name=_('Who are you doing it for?'),
        help_text=TARGET_GROUP_HELP
    )
    local_embedding = models.TextField(
        max_length=800,
        verbose_name=_('Who else, besides the key target group(s), will you '
                       'work with or involve in your project?'),
        help_text=LOCAL_EMBEDDING_HELP
    )
    # not used in current form
    uniqueness = models.TextField(
        blank=True,
        max_length=800,
        verbose_name=_('What makes your idea stand apart in '
                       'its local and regional dimension?'),
        help_text=UNIQUENESS_HELP
    )
    perspective_and_dialog = models.TextField(
        default=_('This question did not exist when this idea was created'),
        max_length=800,
        verbose_name=_('How will you engage different perspectives in '
                       'dialogue around the societal challenge that you '
                       'aim to tackle?'),
        help_text=PERSPECTIVE_AND_DIALOG_HELP
    )

    class Meta:
        abstract = True
