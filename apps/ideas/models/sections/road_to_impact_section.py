from django.db import models
from django.utils.translation import ugettext as _

PLAN_HELP = _('Please describe the activities, specific steps, '
              'methods and approach you will undertake to implement '
              'your project. (max. 1400 characters)')

REACH_OUT_HELP = _('What actions, measures or (communication) channels '
                   'will you use to reach out to your key target groups '
                   'and others to whom your project is relevant? '
                   '(max. 400 characters)')

RESULTS_HELP = _('At the end of your project phase, what will have changed '
                 'for the better thanks to it? (max. 800 characters)')

IMPACT_HELP = _('How will your project help community members get '
                'actively involved in a social or political issue in '
                'their (local) community to improve their quality of '
                'life? How will your project give them a voice in the '
                'decision-making and implementation process? If you are '
                'using the means of civic education: providing '
                'knowledge about institutions, power structures, '
                'policies and processes etc. or skills like debating '
                'etc., please describe them. (max. 800 characters)')

SUSTAINABILITY_HELP = _('What seeds will you plant in order to ensure that '
                        'your initiative continues beyond the project '
                        'funding and that you make an impact? Try to be as '
                        'specific and as realistic as possible. '
                        '(max. 800 characters)')

MOTIVATION_HELP = _('We are looking for people who know the community '
                    'and region they work with, although anyone with a '
                    'solid background can apply. Please introduce your '
                    'project team and briefly summarize their experience '
                    'and skills. Tell us how you are connected to the region '
                    'your idea targets and how you know the specifics of its '
                    'civic landscape.  What motivates you to bring this idea '
                    'to life? What is your connection and mission? '
                    '(max. 800 characters)')


class RoadToImpactSection(models.Model):
    plan = models.TextField(
        max_length=1400,
        help_text=PLAN_HELP,
        verbose_name=_('What is your action plan and how do you '
                       'plan to get there?')
    )
    reach_out = models.TextField(
        max_length=400,
        help_text=REACH_OUT_HELP,
        verbose_name=_('How will you reach out to others?')
    )
    results = models.TextField(
        max_length=800,
        help_text=RESULTS_HELP,
        verbose_name=_('What are the expected results?')
    )
    impact = models.TextField(
        blank=True,
        max_length=800,
        help_text=IMPACT_HELP,
        verbose_name=_('How does your idea strengthen democracy '
                       'and active citizenship at a local and '
                       'community level? Please refer to your '
                       'described challenge. '),
    )
    sustainability = models.TextField(
        max_length=800,
        help_text=SUSTAINABILITY_HELP,
        verbose_name=_('How do you envision the '
                       'sustainability of your initiative?')
    )
    motivation = models.TextField(
        max_length=800,
        help_text=MOTIVATION_HELP,
        verbose_name=_('Who is the team behind the idea '
                       'and why is this cause important to you?')
    )

    class Meta:
        abstract = True
