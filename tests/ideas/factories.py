import factory

from adhocracy4.test.factories import ModuleFactory
from apps.ideas.models import Idea
from tests.factories import UserFactory


class IdeaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Idea

    creator = factory.SubFactory(UserFactory)
    module = factory.SubFactory(ModuleFactory)
    # applicant section
    first_name = factory.Faker('first_name_female')
    last_name = factory.Faker('last_name')
    lead_organisation_status = 'NP'
    year_of_registration = 2002
    # idea section
    title = factory.Faker('name')
    pitch = factory.Faker('text')
    topics = ['ES', 'SI']
    # local dimension section
    location = factory.Faker('city')
    challenge = factory.Faker('text')
    impact = factory.Faker('text')
    target_group = factory.Faker('text')
    # road to impact section
    plan = factory.Faker('text')
    # finances section
    total_budget = factory.Faker('random_number')
    budget_requested = factory.Faker('random_number')
    major_expenses = factory.Faker('text')
    duration = factory.Faker('random_number')

    @factory.post_generation
    def co_workers(self, create, extracted, **kwargs):
        if extracted == []:
            return

        if not extracted:
            user = UserFactory()
            self.co_workers.add(user)
            return

        if extracted:
            for user in extracted:
                if isinstance(user, str):
                    self.co_workers.add(
                        UserFactory(username=user)
                    )
                else:
                    self.co_workers.add(user)

    @factory.post_generation
    def invites(self, create, extracted, **kwargs):
        if not extracted:
            return

        if extracted:
            for email in extracted:
                self.ideainvite_set.invite(
                    creator=self.creator,
                    email=email,
                )
