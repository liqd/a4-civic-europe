import pytest


@pytest.mark.django_db
def test_autofollow_on_create(idea_factory, user):
    idea = idea_factory(co_workers=[user])
    assert idea.ideafollow_set.filter(creator=user)


@pytest.mark.django_db
def test_autofollow_on_update(idea, user):
    idea.co_workers.add(user)
    assert idea.ideafollow_set.filter(creator=user)

    idea.co_workers.remove(user)
    assert not idea.ideafollow_set.filter(creator=user, enabled=True)
    assert idea.ideafollow_set.filter(creator=user, enabled=False)
