from autoslug import AutoSlugField
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from adhocracy4.comments import models as comment_models
from adhocracy4.models import query
from adhocracy4.modules.models import Item
from adhocracy4.ratings import models as rating_models
from apps.follows import register_follow

from .sections.applicant_section import ApplicantSection
from .sections.finances_section import FinancesSection
from .sections.idea_section import IdeaSection
from .sections.local_dimension_section import LocalDimensionSection
from .sections.network_community_section import NetworkSection
from .sections.partners_section import PartnersSection
from .sections.road_to_impact_section import RoadToImpactSection


class IdeaQuerySet(query.RateableQuerySet, query.CommentableQuerySet):
    def filter_by_participant(self, user):
        return self.filter(
            models.Q(creator=user) | models.Q(co_workers=user)
        )


class AbstractIdea(ApplicantSection,
                   PartnersSection,
                   IdeaSection,
                   LocalDimensionSection,
                   RoadToImpactSection,
                   FinancesSection,
                   NetworkSection):

    class Meta:
        abstract = True
        ordering = ['-created']

    def __str__(self):
        return self.title


class Idea(AbstractIdea, Item):
    slug = AutoSlugField(populate_from='title', unique=True)
    is_on_shortlist = models.BooleanField(default=False)
    is_winner = models.BooleanField(default=False)
    jury_statement = models.TextField(
        verbose_name='Why this idea?', blank=True)
    community_award_winner = models.BooleanField(default=False)
    budget_granted = models.IntegerField(null=True, blank=True)
    ratings = GenericRelation(rating_models.Rating,
                              related_query_name='idea',
                              object_id_field='object_pk')
    comments = GenericRelation(comment_models.Comment,
                               related_query_name='idea',
                               object_id_field='object_pk')
    objects = IdeaQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('idea-detail', args=[self.slug])

    @property
    def badge(self):
        if self.is_winner:
            return _('winner')
        if self.community_award_winner:
            return _('community award')
        if self.is_on_shortlist:
            return _('shortlist')


register_follow(Idea)
