import django_filters
from django.utils.translation import ugettext_lazy as _

from adhocracy4.filters import widgets
from adhocracy4.filters.filters import DefaultsFilterSet, FreeTextFilter
from adhocracy4.projects.models import Project

from . import models


class StatusFilterWidget(widgets.DropdownLinkWidget):
    label = _('Status')


class TopicFilterWidget(widgets.DropdownLinkWidget):
    label = _('Topic')

    def __init__(self, attrs=None):
        choices = (('', _('All')),)
        choices += (models.abstracts.idea_section.
                    IDEA_TOPIC_CHOICES)

        super().__init__(attrs, choices)


class ProjectFilterWidget(widgets.DropdownLinkWidget):
    label = _('Year')


class OrderingFilterWidget(widgets.DropdownLinkWidget):
    label = _('Sorting')
    right = True


class FreeTextSearchFilterWidget(widgets.FreeTextFilterWidget):
    label = _('Search')


class IdeaFilterSet(DefaultsFilterSet):

    defaults = {
        'ordering': 'newest',
    }

    idea_topics = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=TopicFilterWidget,
    )

    project = django_filters.ModelChoiceFilter(
        name='module__project__name',
        queryset=Project.objects.all(),
        widget=ProjectFilterWidget,
    )

    def what_status(self, queryset, name, value):
        if value == 'idea_sketch':
            qs = queryset.filter(proposal__isnull=True)
        elif value == 'proposal':
            qs = queryset.filter(proposal__isnull=False)
        elif value == 'community_award':
            qs = queryset.filter(community_award_winner=True)
        elif value == 'shortlist':
            qs = queryset.filter(is_on_shortlist=True)
        elif value == 'winner':
            qs = queryset.filter(is_winner=True)
        else:
            qs = queryset.all()
        return qs

    status = django_filters.ChoiceFilter(
        method='what_status',
        choices=(
            ('idea_sketch', _('Idea Sketch')),
            ('community_award', _('Community Award Winner')),
            ('shortlist', _('Shortlist')),
            ('proposal', _('Proposal')),
            ('winner', _('Winner'))
        ),
        widget=StatusFilterWidget
    )

    ordering = django_filters.OrderingFilter(
        fields=(
            ('-created', 'newest'),
            ('-comment_count', 'comments'),
            ('idea_title', 'title'),
        ),
        choices=(
            ('newest', _('Most Recent')),
            ('comments', _('Most Comments')),
            ('title', _('Alphabetical')),
        ),
        empty_label=None,
        widget=OrderingFilterWidget
    )

    search = FreeTextFilter(
        widget=FreeTextSearchFilterWidget,
        fields=['idea_title',  # idea section
                'idea_subtitle',
                'idea_pitch',
                'idea_location_specify',
                'challenge',
                'outcome',
                'plan',
                'importance',
                'reach_out',
                'first_name',  # applicant section
                'last_name',
                'organisation_name',
                'organisation_website',
                'organisation_country',
                'partner_organisation_1_name',  # partners section
                'partner_organisation_1_website',
                'partner_organisation_1_country',
                'partner_organisation_2_name',
                'partner_organisation_2_website',
                'partner_organisation_2_country',
                'partner_organisation_3_name',
                'partner_organisation_3_website',
                'partner_organisation_3_country',
                'partners_more_info']
    )

    class Meta:
        model = models.Idea
        fields = ['search', 'project', 'status', 'idea_topics', 'ordering']
