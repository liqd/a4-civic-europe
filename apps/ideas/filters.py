from operator import itemgetter

import django_filters
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from adhocracy4.filters import widgets
from adhocracy4.filters.filters import (DefaultsFilterSet,
                                        DistinctOrderingWithDailyRandomFilter,
                                        FreeTextFilter)
from adhocracy4.projects.models import Project

from . import countries, models

STATUS_FILTER_CHOICES = [
    ('community_award', _('Community Award Winner')),
    ('shortlist', _('Shortlist')),
    ('winner', _('Winner'))
]

ORDERING_CHOICES = [
    ('dailyrandom', _('Daily random')),
    ('newest', _('Most recent')),
    ('comments', _('Most comments')),
    ('support', _('Most support')),
    ('title', _('Alphabetical'))
]

EUROPEAN_COUNTRIES = list(countries.EuropeanCountries().countries.items())
EUROPEAN_COUNTRIES.sort(key=itemgetter(1))


class StatusFilterWidget(widgets.DropdownLinkWidget):
    label = _('Status')


class FieldOfActionFilterWidget(widgets.DropdownLinkWidget):
    label = _('Field Of Action')

    def __init__(self, attrs=None):
        choices = (('', _('All')),)
        choices += (models.sections.idea_section.
                    FIELD_OF_ACTION_CHOICES)

        super().__init__(attrs, choices)


class ProjectFilterWidget(widgets.DropdownLinkWidget):
    label = _('Year')


class CountryFilterWidget(widgets.DropdownLinkWidget):
    label = _('Organization Country')

    def __init__(self, attrs=None):
        choices = [('', _('All')), ]
        choices += EUROPEAN_COUNTRIES
        super().__init__(attrs, choices)


class OrderingFilterWidget(widgets.DropdownLinkWidget):
    label = _('Sorting')


class FreeTextSearchFilterWidget(widgets.FreeTextFilterWidget):
    label = _('Search')


class IdeaFilterSet(DefaultsFilterSet):

    defaults = {
        'ordering': 'dailyrandom',
        'status': 'winner',
    }

    field_of_action = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=FieldOfActionFilterWidget,
    )

    project = django_filters.ModelChoiceFilter(
        field_name='module__project__name',
        queryset=Project.objects.all(),
        widget=ProjectFilterWidget,
    )

    def organisation_countries(self, queryset, name, value):
        return queryset.filter(
            Q(lead_organisation_country=value)
            | Q(partner_organisation_1_country=value)
            | Q(partner_organisation_2_country=value)
            | Q(partner_organisation_3_country=value)
        )

    country = django_filters.CharFilter(
        field_name='',
        method='organisation_countries',
        widget=CountryFilterWidget,
    )

    def what_status(self, queryset, name, value):
        if value == 'community_award':
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
        choices=STATUS_FILTER_CHOICES,
        widget=StatusFilterWidget,
        empty_label=_('All ideas')
    )

    ordering = DistinctOrderingWithDailyRandomFilter(
        fields=(
            ('-created', 'newest'),
            ('-comment_count', 'comments'),
            ('-positive_rating_count', 'support'),
            ('title', 'title'),
        ),
        choices=ORDERING_CHOICES,
        empty_label=None,
        widget=OrderingFilterWidget,
    )

    search = FreeTextFilter(
        widget=FreeTextSearchFilterWidget,
        fields=['title',  # idea section
                'subtitle',
                'pitch',
                'challenge',  # local dimension section
                'plan',  # road to impact section
                'feedback',  # network community section
                'first_name',  # applicant section
                'last_name',
                'lead_organisation_name',
                'lead_organisation_website',
                'partner_organisation_1_name',  # partners section
                'partner_organisation_1_website',
                'partner_organisation_2_name',
                'partner_organisation_2_website',
                'partner_organisation_3_name',
                'partner_organisation_3_website',
                'partners_more_info']
    )

    class Meta:
        model = models.Idea
        fields = ['search', 'project', 'status', 'field_of_action', 'country',
                  'ordering']
