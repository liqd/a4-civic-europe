import pytest
from django.urls import reverse

from apps.ideas import views


@pytest.mark.django_db
def test_idea_detail_view(rf, idea_factory):
    idea = idea_factory()

    view = views.IdeaDetailView.as_view()
    request = rf.get('/ideas/')
    response = view(request, slug=idea.slug)
    assert 'idea_list_1' in response.context_data
    assert (response.context_data['idea_list_1'][0] ==
            ('Idea pitch', idea.pitch))
    assert 'partner_list' in response.context_data


@pytest.mark.django_db
def test_idea_edit_form_has_request(admin, idea_factory, client):
    client.login(email=admin.email, password='password')
    idea = idea_factory()
    url = reverse('idea-update-form',
                  kwargs={'slug': idea.slug, 'form_number': '3'})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_proposal_edit_form_has_request(admin, idea_factory, client):
    client.login(email=admin.email, password='password')
    idea = idea_factory()
    url = reverse('idea-update-form',
                  kwargs={'slug': idea.slug, 'form_number': '3'})
    response = client.get(url)
    assert response.status_code == 200
