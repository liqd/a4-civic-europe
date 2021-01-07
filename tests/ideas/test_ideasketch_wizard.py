import pytest
from django.contrib.staticfiles import finders
from django.core import mail
from django.urls import reverse

from apps.ideas.models import Idea
from apps.ideas.phases import IdeaPhase
from tests.helpers import active_phase


@pytest.mark.django_db
def test_ideasketch_create_wizard(client, user, module, image):
    client.login(username=user.email,
                 password='password')
    url = reverse('idea-create',
                  kwargs={'slug': module.slug})

    with active_phase(module, IdeaPhase):

        # Form 1 (Applicant)
        response = client.get(url)
        assert response.status_code == 200

        data = {
            'idea_create_wizard-current_step': '0',
            '0-first_name': 'Qwertz',
            '0-last_name': 'Uiopü',
            '0-lead_organisation_status': 'OT',
        }

        response = client.post(url, data)
        assert response.context['form'].errors == {'lead_organisation_details':
                                                   ["You selected 'other' as "
                                                    "organization status. "
                                                    "Please provide more "
                                                    "information about your "
                                                    "current status."]}
        assert response.status_code == 200

        data = {
            'idea_create_wizard-current_step': '0',
            '0-lead_organisation_details': 'We are great',
            '0-first_name': 'Qwertz',
            '0-last_name': 'Uiopü',
            '0-lead_organisation_status': 'OT'
        }

        # Form 2 (Partners)
        response = client.post(url, data)
        assert response.context['form'].errors == {}
        assert response.status_code == 200

        data = {
            'idea_create_wizard-current_step': '1',
        }

        # Form 3 (Idea details)
        response = client.post(url, data)
        assert response.status_code == 200

        img_file = open(finders.find('images/cta_tile_logo_colour.png'), "rb")

        data = {
            'idea_create_wizard-current_step': '2',
            '2-title': 'My very good idea',
            '2-pitch': 'My very good idea is such a good idea!',
            '2-image': img_file,
            '2-country_of_implementation': 'CZ',
            '2-field_of_action': 'YP'
        }

        response = client.post(url, data)
        assert response.context['form'].errors == {}
        assert response.status_code == 200

        img_file.close()
        img_file2 = open(finders.find('images/cta_tile_logo.png'), "rb")

        data = {
            'idea_create_wizard-current_step': '2',
            '2-title': 'My very good idea',
            '2-subtitle': 'My very good idea - subtitle',
            '2-pitch': 'My very good idea is such a good idea!',
            '2-image': img_file2,
            '2-country_of_implementation': 'CZ',
            '2-field_of_action': 'YP'
        }

        # Form 4 (Local Dimension)
        response = client.post(url, data)
        assert response.context['form'].errors == {}
        assert response.status_code == 200

        img_file2.close()

        data = {
            'idea_create_wizard-current_step': '3',
            '3-location': 'Balance a ball on your nose',
            '3-location_details': 'UA',
            '3-cohesion': 'Because there`re no balls around',
            '3-challenge': 'I balanced a ball on my nose',
            '3-target_group': 'Children',
            '3-local_embedding': 'Children',
            '3-perspective_and_dialog': 'The ball can`t talk',
        }

        # Form 5 (Road to Impact)
        response = client.post(url, data)
        assert response.context['form'].errors == {}
        assert response.status_code == 200

        data = {
            'idea_create_wizard-current_step': '4',
            '4-plan': 'not_sure',
            '4-reach_out': 'Mr. Not So Sure',
            '4-results': 'email@example.com',
            '4-impact': 'I will balance a ball on my nose',
            '4-sustainability': 'We will be very sure afterwards',
            '4-contribution': 'contribution',
            '4-knowledge': 'knowledge',
            '4-motivation': 'motivation'
        }

        # Form 6 (Finance Section)
        response = client.post(url, data)
        assert response.context['form'].errors == {}
        assert response.status_code == 200

        data = {
            'idea_create_wizard-current_step': '5',
            '5-total_budget': 20000,
            '5-budget_requested': 30000,
            '5-major_expenses': 'Food',
            '5-duration': 12
        }

        response = client.post(url, data)
        assert response.context['form'].errors == \
            {'__all__': ["The requested budget can't "
                         "be higher than the total budget"]}

        data = {
            'idea_create_wizard-current_step': '5',
            '5-total_budget': 20000,
            '5-budget_requested': 10000,
            '5-major_expenses': 'Food',
            '5-duration': 12
        }

        # Form 7 (Network and Community Section)
        response = client.post(url, data)
        assert response.context['form'].errors == {}
        assert response.status_code == 200

        data = {
            'idea_create_wizard-current_step': '6',
            '6-network': 'network',
            '6-accept_conditions': True,
            '6-confirm_publicity': True
        }

        # Form 8 (Finish)
        response = client.post(url, data)
        assert response.context['form'].errors == {}
        assert response.status_code == 200
        assert Idea.objects.all().count() == 0

        data = {
            'idea_create_wizard-current_step': '7',
        }

        response = client.post(url, data)
        my_idea = Idea.objects.get(title='My very good idea')

        assert response.status_code == 302
        assert Idea.objects.all().count() == 1
        assert my_idea.first_name == 'Qwertz'
        assert my_idea.target_group == 'Children'
        assert mail.outbox[0].subject == (
            'Welcome and thanks for sharing your idea!'
        )
        assert mail.outbox[0].recipients() == [user.email]
