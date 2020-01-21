import pytest

from apps.ideas import filters, models


@pytest.mark.django_db
def test_idea_list_view(idea_factory):
    idea_factory()
    idea_factory(is_on_shortlist=True)

    ALL_POSSIBLE_PARAMS = [('community_award', 0),
                           ('shortlist', 1),
                           ('winner', 0),
                           ('', 2)]

    idea_filter_set = filters.IdeaFilterSet(data={}, view=None)

    for param, count in ALL_POSSIBLE_PARAMS:
        assert (lambda p: (idea_filter_set.
                           what_status(models.Idea.objects.all(),
                                       'some_name', p)
                           ).count()
                )(param) == count
