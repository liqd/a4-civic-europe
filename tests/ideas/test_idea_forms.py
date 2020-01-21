import pytest
from django import forms

from apps.ideas import forms as idea_forms


@pytest.mark.django_db
@pytest.mark.parametrize('idea__co_workers', [[]])
def test_community_section_empty_edit(idea):
    """
    Check that the CommunitySectionEdit form works if no co-workers and
    and invites are present.
    """

    form = idea_forms.NetworkAndCommunitySectionEditForm(
        instance=idea,
    )

    assert list(idea.co_workers.all()) == []
    assert list(idea.ideainvite_set.all()) == []

    form = idea_forms.NetworkAndCommunitySectionEditForm(
        instance=idea,
        data={
            'co_workers_emails': 'test@test.de, test2@test.de',
            'network': 'edit_network',
            'feedback': 'feedback'
        }
    )

    assert form.is_valid()
    idea = form.save()
    assert idea.network == 'edit_network'
    assert idea.feedback == 'feedback'
    invites = ['test@test.de', 'test2@test.de']
    new_invites = list(
        idea.ideainvite_set.values_list('email', flat=True)
    )
    assert len(new_invites) == len(invites)
    assert 'test@test.de' in new_invites
    assert 'test2@test.de' in new_invites


@pytest.mark.django_db
@pytest.mark.parametrize('idea__invites',
                         [['test@test.de', 'foo@test.de']])
@pytest.mark.parametrize('idea__co_workers', [['Jürgen', 'Erich']])
def test_co_worker_edit(idea):
    """
    Remove co-worker and invite, while also adding new invite all in
    one operation.
    """
    co_workers = list(idea.co_workers.all())
    form = idea_forms.NetworkAndCommunitySectionEditForm(
        instance=idea,
    )

    form = idea_forms.NetworkAndCommunitySectionEditForm(
        instance=idea,
        data={
            'co_workers_emails': 'test1@test.de, test2@test.de',
            'co_workers': ['i:test1@test.de']
        }
    )
    assert not form.is_valid()

    form = idea_forms.NetworkAndCommunitySectionEditForm(
        instance=idea,
        data={
            'co_workers_emails': 'test1@test.de, test2@test.de',
            'co_workers': ['c:Erich', 'i:foo@test.de'],
            'network': 'edit_network',
            'feedback': 'feedback'
        }
    )

    form.is_valid()
    assert not form.errors
    idea = form.save()
    assert idea.network == 'edit_network'
    invites = ['foo@test.de', 'test1@test.de', 'test2@test.de']
    new_invites = list(
        idea.ideainvite_set.values_list('email', flat=True)
    )
    assert len(invites) == len(new_invites)
    for invite in invites:
        assert invite in new_invites
    assert list(idea.co_workers.all()) == co_workers[1:]


@pytest.mark.django_db
@pytest.mark.parametrize('idea__invites',
                         [['test1@test.de', 'test2@test.de', 'test3@test.de']])
@pytest.mark.parametrize('idea__co_workers', [['test4', 'test5']])
def test_co_worker_edit_too_many(idea):
    form = idea_forms.NetworkAndCommunitySectionEditForm(
        instance=idea,
        data={
            'co_workers_emails': 'test6@test.de',
            'network': 'edit_network',
            'feedback': 'feedback',
            'co_workers': ['c:test4', 'c:test5', 'i:test1@test.de',
                           'i:test2@test.de', 'i:test3@test.de'],
        }
    )

    assert not form.is_valid()


@pytest.mark.django_db
@pytest.mark.parametrize('idea__invites',
                         [['test1@test.de', 'test2@test.de', 'test3@test.de']])
@pytest.mark.parametrize('idea__co_workers', [['test4', 'test5']])
def test_co_worker_edit_replace_one(idea):
    form = idea_forms.NetworkAndCommunitySectionEditForm(
        instance=idea,
        data={
            'co_workers_emails': 'test6@test.de',
            'network': 'edit_network',
            'feedback': 'feedback',
            'co_workers': ['c:test4', 'i:test1@test.de',
                           'i:test2@test.de', 'i:test3@test.de'],
        }
    )

    assert form.is_valid()


@pytest.mark.django_db
@pytest.mark.parametrize('idea__invites', [['test@test.de']])
def test_collaborators_reinvite(idea):
    form = idea_forms.NetworkAndCommunitySectionEditForm(
        instance=idea,
        data={
            'co_workers_emails': 'test@test.de',
            'network': 'edit_network',
            'feedback': 'feedback',
            'co_workers': ['i:test@test.de'],
        }
    )

    assert not form.is_valid()


def test_clean_co_workers_email():

    class TestForm(idea_forms.CoWorkersEmailsFormMixin, forms.Form):
        co_workers_emails = forms.CharField()

    form = TestForm(
        data={'co_workers_emails': 'meg@test.com, carren@test.de'}
    )
    assert form.is_valid()

    form = TestForm(data={'co_workers_emails': 'meg, carren@test.de, john'})
    assert not form.is_valid()
    assert form.errors == {
        'co_workers_emails': [
            'Invalid email address (meg)',
            'Invalid email address (john)'
        ]
    }

    form = TestForm(
        data={'co_workers_emails': 'carren@test.de, carren@test.de'}
    )
    assert not form.is_valid()
    assert form.errors == {
        'co_workers_emails': [
            'Duplicate email address (carren@test.de)',
        ]
    }
