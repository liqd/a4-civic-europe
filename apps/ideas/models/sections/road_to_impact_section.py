from django.db import models
from django.utils.translation import ugettext as _

PLAN_HELP = _('Please describe the specific steps, '
              'interventions, methods and/or approach you will '
              'undertake to implement your project idea. '
              '(max. 800 characters)')

REACH_OUT_HELP = _('Through what actions, measures or channels will '
                   'you be reaching out to your key target groups and '
                   'others to whom your project idea is relevant? '
                   '(max. 800 characters)')

RESULTS_HELP = _('If your idea is selected, what will be different '
                 'a year from now? What would success look like for '
                 'you? Think back to the challenge your project is '
                 'addressing - what will have changed, in part, '
                 'thanks to your project? How is the local '
                 'community empowered? (max. 800 characters)')

SUSTAINABILITY_HELP = _('What actions or next steps will you take '
                        'in order to ensure that your initiative '
                        'continues beyond the project funding?')

CONTRIBUTION_HELP = _('Please share how your idea relates to the '
                      'bigger picture and strengthens democracy '
                      'in Europe. (max. 800 characters)')

KNOWLEDGE_HELP = _('We are looking for people that know the '
                   'community and region they are working with, '
                   'although everybody with a solid background can '
                   'apply. Please introduce your project team and briefly '
                   'summarise their experience and skills. Tell us how you '
                   'are connected to the region your idea will take place '
                   'in and how do you know about the specificities of its '
                   'civic landscape. (max. 800 characters).')

MOTIVATION_HELP = _('What motivates you to bring this idea to life? '
                    'What is your connection and mission '
                    'behind the idea? (max. 800 characters)')


class RoadToImpactSection(models.Model):

    plan = models.TextField(
        max_length=800,
        help_text=PLAN_HELP,
        verbose_name=_('How do you plan to get there?'))

    reach_out = models.TextField(
        max_length=800,
        help_text=REACH_OUT_HELP,
        verbose_name=_('How will you be reaching out to others '
                       'and advocating your project idea?'))

    results = models.TextField(
        max_length=800,
        help_text=RESULTS_HELP,
        verbose_name=_('What are the expected results?'))

    sustainability = models.TextField(
        max_length=800,
        help_text=SUSTAINABILITY_HELP,
        verbose_name=_('How will you ensure the '
                       'sustainability of your '
                       'initiative?'))

    contribution = models.TextField(
        max_length=800,
        help_text=CONTRIBUTION_HELP,
        verbose_name=_('How does your initiative '
                       'contribute to strengthening '
                       'democracy in Europe? '))

    knowledge = models.TextField(
        max_length=800,
        help_text=KNOWLEDGE_HELP,
        verbose_name=_('Why are you the right people '
                       'for responding to this challenge?'))

    motivation = models.TextField(
        max_length=800,
        help_text=MOTIVATION_HELP,
        verbose_name=_('Why is this idea '
                       'important to you?'))

    class Meta:
        abstract = True
