import django_filters
from django.utils.translation import ugettext_lazy as _

from adhocracy4.filters import widgets
from adhocracy4.filters.filters import DefaultsFilterSet

from apps.ideas import models as idea_models


class ParticipationFilterWidget(widgets.DropdownLinkWidget):
    label = _('Participation')


class OrderingFilterWidget(widgets.DropdownLinkWidget):
    label = _('Sorting')
    right = True


class ProfileIdeaFilterSet(DefaultsFilterSet):

    defaults = {
        'ordering': 'newest',
        'participation': 'creator',
    }

    class Meta:
        model = idea_models.Idea
        fields = ['participation', 'ordering']

    def __init__(self, user, data, *args, **kwargs):
        data = data.copy()
        self.user = user

        # Set the defaults if they are not manually set yet
        for key, value in self.defaults.items():
            if key not in data:
                data[key] = value

        super(django_filters.FilterSet, self).__init__(data, *args, **kwargs)

    def participation_filter(self, queryset, name, value):
        if value == 'creator':
            return queryset.filter(creator=self.user)
        elif value == 'collaborator':
            return queryset.filter(collaborators=self.user)
        elif value == 'supporter':
            return queryset.filter(
                ratings__creator=self.user,
                ratings__value=1)
        elif value == 'comment':
            return queryset.filter(comments__creator=self.user)
        elif value == 'watcher':
            return queryset.filter(
                ideafollow__creator=self.user,
                ideafollow__enabled=True,
            )
        else:
            return queryset.filter_by_participant(self.user)

    participation = django_filters.ChoiceFilter(
        method='participation_filter',
        choices=(
            ('creator', _('Submitted')),
            ('collaborator', _('Collaborator')),
            ('watcher', _('Watching')),
            ('supporter', _('Supporting')),
            ('comment', _('Comments'))
        ),
        empty_label=None,
        widget=ParticipationFilterWidget,
    )

    ordering = django_filters.OrderingFilter(
        fields=(
            ('-created', 'newest'),
            ('created', 'oldest'),
        ),
        choices=(
            ('newest', _('Newest')),
            ('oldest', _('Oldest')),
        ),
        empty_label=None,
        widget=OrderingFilterWidget
    )
