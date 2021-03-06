import factory
from django.conf import settings
from django.contrib.auth.hashers import make_password


class OrganisationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'a4organisations.Organisation'
        django_get_or_create = ('name',)

    name = factory.Faker('company')


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = settings.AUTH_USER_MODEL

    username = factory.Sequence(lambda n: 'user%d' % n)
    password = make_password('password')
    email = factory.Faker('email')


class AdminFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = settings.AUTH_USER_MODEL

    username = factory.Faker('name')
    password = make_password('password')
    is_superuser = True
    is_staff = True
