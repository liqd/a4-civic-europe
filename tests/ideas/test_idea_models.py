import pytest

from apps.ideas import models


@pytest.mark.django_db
def test_with_participant(idea_factory, user):
    idea1 = idea_factory(creator=user)
    idea2 = idea_factory(co_workers=[user])
    idea_factory()

    result = models.Idea.objects.filter_by_participant(user)
    assert list(result) == [idea2.idea, idea1.idea]
