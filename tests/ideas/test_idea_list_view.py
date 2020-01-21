import pytest
from django.urls import reverse

from apps.ideas import phases
from tests.helpers import active_phase


@pytest.mark.django_db
def test_idea_list_view(client, idea_factory):
    idea_factory()
    idea_factory()
    idea_factory()

    url = reverse('idea-list')
    response = client.get(url)
    # default filter settings for the idea filters are 'status': 'winner'
    assert len(response.context_data['object_list']) == 0
    assert response.status_code == 200

    response = client.get(url + '?topics=environment&ordering=newest&'
                          'project=&status=')
    assert len(response.context_data['object_list']) == 3
    assert response.status_code == 200


@pytest.mark.django_db
def test_idea_list_view_idea_phase(client, idea_factory, module):
    url = reverse('idea-list')

    # the default filters for the ideaSketchPhase set
    # 'status': 'idea' and the year (project) to the active one
    with active_phase(module, phases.IdeaPhase):
        idea_factory(module=module)
        idea_factory(module=module)

        response = client.get(url)
        assert len(response.context_data['object_list']) == 2
        assert response.status_code == 200

        response = client.get(url + '?topics=environment&ordering=newest&'
                              'project=&status=')
        assert len(response.context_data['object_list']) == 2
        assert response.status_code == 200
