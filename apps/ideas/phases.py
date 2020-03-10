from django.http import QueryDict
from django.utils.translation import ugettext_lazy as _

from adhocracy4 import phases

from . import apps, models


class IdeaPhase(phases.PhaseContent):
    app = apps.Config.label
    weight = 10
    view = None

    module_name = _('Civic Europe')

    def get_phase_filters(self, active_project_pk):
        if 'project' in self.default_filters:
            self.default_filters['project'] = str(active_project_pk)
        return self.default_filters


class PreCallPhase(IdeaPhase):
    phase = 'pre_call'

    name = _('Pre call phase')
    description = _(
        'get an idea how the idea challenge is run'
    )

    default_filters = QueryDict('ordering=newest&'
                                'status=winner',
                                mutable=True
                                )


phases.content.register(PreCallPhase())


class IdeaPhase(IdeaPhase):
    phase = 'ideas'

    name = _('Idea phase')
    description = _(
        'issue and edit ideas, but also collect some early feedback'
    )
    module_name = _('Civic Europe')

    features = {
        'crud': (models.Idea,),
    }

    default_filters = QueryDict('ordering=newest&'
                                'status=&'
                                'project=',
                                mutable=True
                                )


phases.content.register(IdeaPhase())


class InterimPostSketchPhase(IdeaPhase):
    phase = 'interim_post_sketch'

    name = _('Interim post sketch phase')
    description = _(
        'submitting of idea sketches is closed'
    )

    default_filters = QueryDict('ordering=newest&'
                                'status=&'
                                'project=',
                                mutable=True
                                )


phases.content.register(InterimPostSketchPhase())


class CommunityAwardRatingPhase(IdeaPhase):
    phase = 'community_award_rating'

    name = _('Community award rating')
    description = _('submit your rating for the community award')
    module_name = _('Civic Europe')

    features = {
        'rate': (models.Idea,),
        # rating only for users, that added an idea in this (or previous) years
    }

    default_filters = QueryDict('ordering=comments&'
                                'status=&'
                                'project=',
                                mutable=True
                                )


phases.content.register(CommunityAwardRatingPhase())


class InterimShortlistSelectionPhase(IdeaPhase):
    phase = 'interim_shortlist_selection'

    name = _('Interim shortlist selection phase')
    description = _('ideas for the shortlist are chosen by the jury')

    default_filters = QueryDict('ordering=support&'
                                'status=&'
                                'project=',
                                mutable=True
                                )


phases.content.register(InterimShortlistSelectionPhase())


class InterimShortlistPublicationPhase(IdeaPhase):
    phase = 'interim_shortlist_publication'

    name = _('Interim shortlist publication phase')
    description = _('the shortlist is published')

    default_filters = QueryDict('ordering=title&'
                                'status=shortlist&project=',
                                mutable=True
                                )


phases.content.register(InterimShortlistPublicationPhase())


class InterimWinnersPhase(IdeaPhase):
    phase = 'interim_winners'

    name = _('Interim winners phase')
    description = _('winning ideas are from the current idea '
                    'challenge are shown')

    default_filters = QueryDict('ordering=newest&'
                                'status=winner&'
                                'project=',
                                mutable=True
                                )


phases.content.register(InterimWinnersPhase())
