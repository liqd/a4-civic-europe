from django import template

from apps.ideas.filters import IdeaFilterSet
from apps.ideas.models import Idea

register = template.Library()


@register.simple_tag(takes_context=False)
def load_ideas(year, field_of_action, ordering, status):

    ideas = Idea.objects.all()\
        .annotate_comment_count()\
        .annotate_positive_rating_count()
    idea_filter_set = IdeaFilterSet(data={}, view=None)

    if year:
        ideas = idea_filter_set.filters['project'].filter(ideas, year)
    if field_of_action:
        ideas = idea_filter_set.filters['field_of_action']\
            .filter(ideas, field_of_action)
    if ordering:
        ideas = idea_filter_set.filters['ordering'].filter(ideas, [ordering])
    if status:
        ideas = idea_filter_set.filters['status'].filter(ideas, status)

    return ideas[:20]
