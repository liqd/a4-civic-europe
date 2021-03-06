from django.apps import AppConfig

from adhocracy4.actions.verbs import Verbs


class Config(AppConfig):
    name = 'apps.actions'
    label = 'civic_europe_actions'

    def ready(self):
        from adhocracy4.actions.models import configure_icon, configure_type
        configure_type('project', ('a4projects', 'project'))
        configure_type('phase', ('a4phases', 'phase'))
        configure_type(
            'comment',
            ('a4comments', 'comment'),
            ('civic_europe_ideas', 'idea'),
        )
        configure_type('rating', ('a4ratings', 'rating'))
        configure_type(
            'idea',
            ('civic_europe_ideas', 'idea'),
        )
        configure_type('blog', ('cms_blog', 'blogpage'))
        configure_type('journey entry',
                       ('civic_europe_journeys', 'journeyentry'))
        configure_type('follows', ('civic_europe_ideas', 'ideafollow'))

        configure_icon('comment', type='comment')
        configure_icon('lightbulb-o', type='item')
        configure_icon('plus', verb=Verbs.ADD)
        configure_icon('pencil', verb=Verbs.UPDATE)
        configure_icon('flag', verb=Verbs.START)
        configure_icon('clock-o', verb=Verbs.SCHEDULE)
