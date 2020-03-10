import pytest


@pytest.mark.django_db
def test_fallback_avatar(user):
    avatar_path = '/static/images/avatar-0{}.svg'.format(user.pk % 3)
    assert user.fallback_avatar == avatar_path


@pytest.mark.django_db
def test_avatar_or_fallback_url(user):
    avatar_path = '/static/images/avatar-0{}.svg'.format(user.pk % 3)
    assert user.avatar_or_fallback_url() == avatar_path


@pytest.mark.django_db
def test_is_innovator(user, idea_factory):
    assert not user.is_innovator
    idea = idea_factory(co_workers=[user])
    assert user.is_innovator
    idea.delete()
    assert not user.is_innovator
    idea_factory(creator=user)
    assert user.is_innovator
