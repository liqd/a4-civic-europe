from django.db import models
from django.utils.translation import ugettext as _
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField

from adhocracy4.images import fields
from apps.ideas.countries import EuropeanCountries

COMMUNITY_DEVELOPMENT = 'CD'
SOCIAL_INCLUSION = 'SI'
ENVIRONMENT_AND_SUSTAINABILITY = 'ES'
ARTS_AND_CULTURAL_ACTIVITIES = 'AC'
HUMAN_RIGHTS = 'HR'
YOUTH_PARTICIPATION = 'YP'
JOURNALISM = 'JL'
SOCIAL_ENTREPRENEURSHIP = 'SE'
OTHER = 'OT'

FIELD_OF_ACTION_CHOICES = (
    (COMMUNITY_DEVELOPMENT, _('Community development')),
    (SOCIAL_INCLUSION, _('Social inclusion')),
    (ENVIRONMENT_AND_SUSTAINABILITY, _('Environment and sustainability')),
    (ARTS_AND_CULTURAL_ACTIVITIES, _('Arts and cultural activities')),
    (HUMAN_RIGHTS, _('Human rights')),
    (YOUTH_PARTICIPATION, _('Youth participation and empowerment')),
    (JOURNALISM, _('Journalism')),
    (SOCIAL_ENTREPRENEURSHIP, _('(Social) Entrepreneurship')),
    (OTHER, _('Other'))
)

TITLE_HELP = _('Give your idea a short and '
               'meaningful title (max. 50 characters). For instance: '
               '“Islands of Hope”')
SUBTITLE_HELP = _('Here you can add a short explanation of your title '
                  '(max. 200 characters). For instance: “Fostering a '
                  'culture of democratic dialogue and co-designing a '
                  'vision for the development of a small island.”')
PITCH_HELP = _('Share a concise and appealing text that summarizes your '
               'idea, makes the reader want to learn more and that is '
               'memorable. Summarize the challenge you are tackling, '
               'your objective, target group and approach in 3-5 '
               'sentences. (max. 500 characters)')
IMAGE_HELP = _('Upload a photo or illustration that visually supports '
               'or explains your idea. The picture will not influence '
               'the selection process but it will be used as a header '
               'picture of your idea on the website. Make sure that you '
               'have the property rights to share this picture. You can '
               'upload a .jpg, .png or .gif up to 3 MB in size. '
               'The image should be in landscape (not portrait) format '
               'and have a width of at least 400 pixels.')
COUNTRY_OF_IMPLEMENTATION_HELP = _('You can choose multiple options if your '
                                   'project takes place in more than one '
                                   'country.')
FIELD_OF_ACTION_HELP = _('Project ideas should be based on democratic values '
                         'like human dignity, tolerance, freedom and '
                         'diversity of opinion and the rule of law. They '
                         'should also strengthen civic engagement and '
                         'participation, ideally by means of civic '
                         'education. Please choose 1-2 of the fields below '
                         'that suit your idea. This will not influence the '
                         'selection process, but will help users to filter '
                         'the ideas in the idea space.')


class IdeaSection(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name=_('Idea title'),
        help_text=TITLE_HELP
    )
    subtitle = models.CharField(
        max_length=200,
        verbose_name=_('Idea subtitle'),
        help_text=SUBTITLE_HELP,
        blank=True
    )
    pitch = models.TextField(
        max_length=500,
        verbose_name=_('Idea pitch'),
        help_text=PITCH_HELP
    )
    image = fields.ConfiguredImageField(
        'image',
        upload_to='ideas/images',
        verbose_name=_('Visualise your idea'),
        help_text=IMAGE_HELP,
    )
    country_of_implementation = CountryField(
        countries=EuropeanCountries,
        help_text=COUNTRY_OF_IMPLEMENTATION_HELP,
        multiple=True
    )
    field_of_action = MultiSelectField(
        max_length=255,
        choices=FIELD_OF_ACTION_CHOICES,
        max_choices=2,
        help_text=FIELD_OF_ACTION_HELP
    )
    field_of_action_other = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_('If you chose “Other” please specify briefly here'),
        help_text=_('(max. 50 characters)')
    )

    class Meta:
        abstract = True

    @property
    def idea_field_of_action_names(self):
        choices = dict(FIELD_OF_ACTION_CHOICES)
        return [choices[action] for action in
                self.field_of_action if action != 'OT']

    @property
    def all_idea_field_of_action_names(self):
        idea_field_of_actions = self.idea_field_of_action_names
        if self.field_of_action_other:
            idea_field_of_actions.append(self.field_of_action_other)
        return idea_field_of_actions
