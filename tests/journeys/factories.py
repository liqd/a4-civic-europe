import factory

from apps.journeys.models import JourneyEntry
from tests.factories import UserFactory
from tests.ideas.factories import IdeaFactory


class JourneyEntryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = JourneyEntry

    idea = factory.SubFactory(IdeaFactory, is_winner=True)
    title = factory.Faker('name')
    category = 'he'
    text = factory.Faker('text')
    creator = factory.SubFactory(UserFactory)
