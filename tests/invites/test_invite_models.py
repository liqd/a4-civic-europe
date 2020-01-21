import pytest
from django.core import mail
from faker import Faker

from apps.invites.models import IdeaInvite

fake = Faker()


@pytest.mark.django_db
def test_invite_on_quyerset(user, idea):
    email = fake.email()

    IdeaInvite.objects.invite(user, email, subject=idea)
    assert mail.outbox[-1].to == [email]

    email = fake.email()
    invite = idea.ideainvite_set.invite(user, email)
    assert mail.outbox[-1].to == [email]
    assert invite.subject == idea


@pytest.mark.django_db
def test_accept(invite, user):
    invite.accept(user)
    assert user in invite.subject.co_workers.all()
    assert not IdeaInvite.objects.filter(token=invite.token)


@pytest.mark.django_db
def test_reject(invite, user):
    invite.reject()
    assert user not in invite.subject.co_workers.all()
    assert not IdeaInvite.objects.filter(token=invite.token)
