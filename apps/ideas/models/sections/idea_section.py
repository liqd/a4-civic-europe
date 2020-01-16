from django.db import models
from django.utils.translation import ugettext as _
from multiselectfield import MultiSelectField

from adhocracy4.images import fields

TITLE_HELP = _('Give your idea a short and '
               'meaningful title (max. 50 characters).')
PITCH_HELP = _('Share a concise and '
               'appealing text that makes the reader curious. '
               'Summarise your main challenge, objective, '
               'target group, approach or activities, and intended '
               'impact in 3-5 sentences. (max. 500 characters)')
IMAGE_HELP = _('Upload a photo or illustration that visually '
               'supports or explains your idea. '
               'Make sure that you have the property rights '
               'to share this picture. You can '
               'upload a .jpg, .png or .gif up to 3 MB in size. '
               'The image should be in '
               'landscape (not portrait) format and have a width '
               'of at least 400 pixels.')

DEMOCRACY_AND_PARTICIPATION = 'DP'
CIVIC_EDUCATION = 'CE'
COMMUNITY_DEVELOPMENT = 'CD'
URBAN_AND_RURAL_PLANING = 'UP'
SOCIAL_INCLUSION = 'SI'
MIGRATION = 'MI'
ENVIRONMENT_AND_SUSTAINABILITY = 'ES'
ARTS_AND_CULTURAL_ACTIVITIES = 'AC'

TOPIC_CHOICES = (
    (DEMOCRACY_AND_PARTICIPATION, _('Democracy and participation')),
    (CIVIC_EDUCATION, _('Civic education')),
    (COMMUNITY_DEVELOPMENT, _('Community development')),
    (URBAN_AND_RURAL_PLANING, _('Urban and rural development')),
    (SOCIAL_INCLUSION, _('Social inclusion')),
    (MIGRATION, _('Migration')),
    (ENVIRONMENT_AND_SUSTAINABILITY, _('Environment & sustainability')),
    (ARTS_AND_CULTURAL_ACTIVITIES, _('Arts and cultural activities'))
)

TOPIC_HELP = _('Choose 1-2 topics that fit to your idea. Your answer '
               'to this question does not influence the selection process. '
               'It helps to get a better overview of the ideas.')


class IdeaSection(models.Model):
    title = models.CharField(
        max_length=50,
        help_text=TITLE_HELP)
    subtitle = models.CharField(
        max_length=200,
        help_text=_('(max. 200 characters)'),
        blank=True)
    pitch = models.TextField(
        max_length=500,
        help_text=PITCH_HELP
    )
    image = fields.ConfiguredImageField(
        'image',
        upload_to='ideas/images',
        blank=True,
        verbose_name=_('Visualise your idea'),
        help_text=IMAGE_HELP
    )
    topics = MultiSelectField(
        max_length=255,
        choices=TOPIC_CHOICES,
        max_choices=2,
        help_text=TOPIC_HELP,
        verbose_name=_('Topic')
    )
    topics_other = models.CharField(
        max_length=250,
        blank=True,
        verbose_name=_('Other'),
        help_text=_('Please specify. (max 250 characters)')
    )

    class Meta:
        abstract = True

    @property
    def idea_topics_names(self):
        choices = dict(TOPIC_CHOICES)
        return [choices[topic] for topic in self.topics]

    @property
    def all_idea_topics_names(self):
        idea_topics = self.idea_topics_names
        if self.topics_other:
            idea_topics.append(self.topics_other)
        return idea_topics
