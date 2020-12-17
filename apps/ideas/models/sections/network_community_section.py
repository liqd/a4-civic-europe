from django.db import models
from django.utils.translation import ugettext as _

NETWORK_HELP = _('Winning projects meet at least one'
                 ' time per year in network meetings and '
                 'receive mentoring and support from the '
                 'Civic Europe team. Tell us about your expectations. '
                 'Think about your skills, resources, networks and '
                 'partners when describing what you could offer and '
                 'what you would like to take away. (max. 800 characters)')

FEEDBACK_HELP = _('What kind of advice, comments or feedback '
                  'would you like to receive about your idea '
                  'from others on the platform? (max. 300 characters)')


class NetworkSection(models.Model):

    network = models.TextField(
        max_length=800,
        help_text=NETWORK_HELP,
        verbose_name=_('How will you contribute to and '
                       'benefit from the Civic Europe network? '))
    feedback = models.TextField(
        max_length=300,
        blank=True,
        help_text=FEEDBACK_HELP,
        verbose_name=_('Reach out – get feedback, '
                       'ideas and inspiration '
                       'from the Civic Europe online '
                       'community!'))

    class Meta:
        abstract = True
