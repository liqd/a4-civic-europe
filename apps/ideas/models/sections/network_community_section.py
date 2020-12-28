from django.db import models
from django.utils.translation import ugettext as _

NETWORK_HELP = _('Winning projects meet at least '
                 'once per year in network meetings '
                 'and participate in peer-to-peer '
                 'learning activities as well as '
                 'trainings. Think about your skills, '
                 'resources, networks and partners when '
                 'describing what you could offer and '
                 'what you would like to take away from '
                 'such network meetings. (max. 800 characters)')

FEEDBACK_HELP = _('Shortened versions of all ideas will be '
                  'published in our idea space, an open space '
                  'where registered users can comment on the '
                  'ideas. What kind of advice, comments or '
                  'feedback would you like to receive about '
                  'your idea from others on the platform? '
                  '(max. 300 characters)')


class NetworkSection(models.Model):

    network = models.TextField(
        max_length=800,
        help_text=NETWORK_HELP,
        verbose_name=_('How will you contribute to and '
                       'benefit from the Civic Europe network?'))
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
