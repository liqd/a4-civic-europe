import pytest
import rules

from apps.ideas import phases
from tests.factories import UserFactory
from tests.helpers import active_phase


@pytest.mark.django_db
def test_idea_view_rule(user):
    assert rules.has_perm('civic_europe_ideas.view_idea',
                          user)


@pytest.mark.django_db
def test_idea_follow_rule(user):
    assert rules.has_perm('civic_europe_ideas.follow_idea',
                          user)


@pytest.mark.django_db
def test_idea_export_rule(admin, user, module):
    assert not rules.has_perm('civic_europe_ideas.export_idea',
                              user)
    user.is_staff = True
    user.save()
    assert rules.has_perm('civic_europe_ideas.export_idea',
                          user)
    assert rules.has_perm('civic_europe_ideas.export_idea',
                          admin)


@pytest.mark.django_db
def test_idea_add_rule(admin, user, module):
    assert not rules.has_perm('civic_europe_ideas.add_idea',
                              user,
                              module)
    assert rules.has_perm('civic_europe_ideas.add_idea',
                          admin,
                          module)


@pytest.mark.django_db
def test_idea_add_rule_idea_phase(user, module):
    with active_phase(module, phases.IdeaPhase):
        assert rules.has_perm('civic_europe_ideas.add_idea',
                              user,
                              module)


@pytest.mark.django_db
def test_idea_add_rule_idea_community_rating_phase(user, module):
    with active_phase(module, phases.CommunityAwardRatingPhase):
        assert not rules.has_perm('civic_europe_ideas.add_idea',
                                  user,
                                  module)


@pytest.mark.django_db
def test_idea_rate_rules(admin, user, idea_factory, module):
    idea = idea_factory(module=module)
    user = UserFactory()
    assert not rules.has_perm('civic_europe_ideas.rate_idea',
                              user,
                              idea)
    idea.creator = user
    assert not rules.has_perm('civic_europe_ideas.rate_idea',
                              user,
                              idea)
    idea.co_workers.add(user)
    assert not rules.has_perm('civic_europe_ideas.rate_idea',
                              user,
                              idea)

    user2 = UserFactory()
    idea2 = idea_factory(creator=user2, module=module)

    with active_phase(module, phases.CommunityAwardRatingPhase):
        assert not rules.has_perm('civic_europe_ideas.rate_idea',
                                  user,
                                  idea)
        assert not rules.has_perm('civic_europe_ideas.rate_idea',
                                  user,
                                  idea2)


@pytest.mark.django_db
def test_journey_rules(admin, user, idea_factory):
    idea = idea_factory()
    creator = UserFactory()
    idea.creator = creator
    co_worker = UserFactory()
    idea.co_workers.set([co_worker])

    # proposal not winner
    assert not rules.has_perm('civic_europe_ideas.add_journey',
                              user, idea)
    assert not rules.has_perm('civic_europe_ideas.add_journey',
                              creator, idea)
    assert not rules.has_perm('civic_europe_ideas.add_journey',
                              co_worker, idea)
    assert rules.has_perm('civic_europe_ideas.add_journey',
                          admin, idea)

    # proposal is winner!
    idea.is_winner = True
    assert not rules.has_perm('civic_europe_ideas.add_journey',
                              user, idea)
    assert rules.has_perm('civic_europe_ideas.add_journey',
                          creator, idea)
    assert rules.has_perm('civic_europe_ideas.add_journey',
                          co_worker, idea)
    assert rules.has_perm('civic_europe_ideas.add_journey',
                          admin, idea)
