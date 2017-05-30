import pytest
from django.core.urlresolvers import reverse
from apps.ideas.models import IdeaSketch, IdeaSketchArchived, Proposal
from apps.ideas.phases import FullProposalPhase

from tests.helpers import active_phase


@pytest.mark.django_db
def test_proposal_anonymous_cannot_create_wizard(client, idea_sketch_factory):
    idea_sketch = idea_sketch_factory(visit_camp=True)
    url = reverse('idea-sketch-add-proposal',
                  kwargs={'slug': idea_sketch.slug})

    with active_phase(idea_sketch.module, FullProposalPhase):
        response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_proposal_random_user_cannot_create_wizard(client, user,
                                                   idea_sketch_factory):
    idea_sketch = idea_sketch_factory(visit_camp=True)
    client.login(username=user.email,
                 password='password')
    url = reverse('idea-sketch-add-proposal',
                  kwargs={'slug': idea_sketch.slug})

    with active_phase(idea_sketch.module, FullProposalPhase):
        response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_proposal_no_camp_cannot_create_wizard(client, user,
                                               idea_sketch_factory):
    idea_sketch = idea_sketch_factory(visit_camp=False)
    idea_sketch.collaborators.add(user)
    client.login(username=user.email,
                 password='password')
    url = reverse('idea-sketch-add-proposal',
                  kwargs={'slug': idea_sketch.slug})

    with active_phase(idea_sketch.module, FullProposalPhase):
        response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_proposal_no_phase_cannot_create_wizard(client, user,
                                                idea_sketch_factory):
    idea_sketch = idea_sketch_factory(visit_camp=True)
    idea_sketch.collaborators.add(user)
    client.login(username=user.email,
                 password='password')
    url = reverse('idea-sketch-add-proposal',
                  kwargs={'slug': idea_sketch.slug})

    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_proposal_collaborator_create_wizard(client,
                                             idea_sketch_factory,
                                             user, image):
    idea_sketch = idea_sketch_factory(visit_camp=True, idea_image=image)
    idea_sketch.collaborators.add(user)
    client.login(username=user.email,
                 password='password')
    url = reverse('idea-sketch-add-proposal',
                  kwargs={'slug': idea_sketch.slug})

    assert IdeaSketchArchived.objects.all().count() == 0
    assert IdeaSketch.objects.all().count() == 1
    assert Proposal.objects.all().count() == 0

    with active_phase(idea_sketch.module, FullProposalPhase):

        # Form 1 (Applicant)
        response = client.get(url)
        wizard = response.context['wizard']
        assert response.status_code == 200
        assert wizard['steps'].count == 6
        assert wizard['steps'].step1 == 1
        for field, value in wizard['form'].initial.items():
            assert str(value) == getattr(idea_sketch, field)
        data = {
            'proposal_create_wizard-current_step': '0'
        }
        for key, value in wizard['form'].initial.items():
            data['0-{}'.format(key)] = value

        # Form 2 (Partners)
        response = client.post(url, data)
        assert response.status_code == 200
        wizard = response.context['wizard']
        assert wizard['steps'].step1 == 2
        for field, value in wizard['form'].initial.items():
            assert str(value) == getattr(idea_sketch, field)
        data = {
            'proposal_create_wizard-current_step': '1'
        }
        for key, value in wizard['form'].initial.items():
            data['1-{}'.format(key)] = value

        # Form 3 (Idea)
        response = client.post(url, data)
        assert response.status_code == 200
        wizard = response.context['wizard']
        assert wizard['steps'].step1 == 3
        for field, value in wizard['form'].initial.items():
            if type(value) is list:
                value = ','.join(value)
            assert value == getattr(idea_sketch, field)
        data = {
            'proposal_create_wizard-current_step': '2'
        }
        for key, value in wizard['form'].initial.items():
            data['2-{}'.format(key)] = value

        # Form 4 (Impact)
        response = client.post(url, data)
        assert response.status_code == 200
        wizard = response.context['wizard']

        assert wizard['steps'].step1 == 4

        for field, value in wizard['form'].initial.items():
            if type(value) is list:
                value = ','.join(value)
            assert value == getattr(idea_sketch, field)
        data = {
            'proposal_create_wizard-current_step': '3'
        }
        for key, value in wizard['form'].initial.items():
            data['3-{}'.format(key)] = value

        # Form 5 (Finances and Duration)
        response = client.post(url, data)
        assert response.status_code == 200
        wizard = response.context['wizard']
        assert wizard['steps'].step1 == 5

        data = {
            'proposal_create_wizard-current_step': '4',
            '4-total_budget': 6000,
            '4-budget_requested': 5000,
            '4-major_expenses': 'Lorem ipsum ...',
            '4-other_sources': 1,
            '4-other_sources_secured': 1,
            '4-duration': 24
        }

        # Form 6 (Community)
        response = client.post(url, data)
        assert response.status_code == 200
        wizard = response.context['wizard']
        assert wizard['steps'].step1 == 6

        for field, value in wizard['form'].initial.items():
            assert value == getattr(idea_sketch, field)

        data = {
            'proposal_create_wizard-current_step': '5',
            '5-accept_conditions': 'on'
        }

        for key, value in wizard['form'].initial.items():
            data['5-{}'.format(key)] = value

        # Final Post
        response = client.post(url, data)
        assert response.status_code == 302
        assert Proposal.objects.all().count() == 1
        assert IdeaSketchArchived.objects.all().count() == 1
        assert IdeaSketch.objects.all().count() == 1

        assert (Proposal.objects.all().first().idea_title
                == idea_sketch.idea_title)
