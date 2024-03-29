import re
from urllib.parse import quote

from allauth.account.adapter import DefaultAccountAdapter
from django.utils.http import url_has_allowed_host_and_scheme

from adhocracy4.emails import Email
from adhocracy4.emails.mixins import SyncEmailMixin
from apps.users import USERNAME_REGEX


class AccountEmail(SyncEmailMixin, Email):
    def get_receivers(self):
        return [self.object]

    @property
    def template_name(self):
        return self.kwargs['template_name']


class AccountAdapter(DefaultAccountAdapter):
    username_regex = re.compile(USERNAME_REGEX)

    def get_email_confirmation_url(self, request, emailconfirmation):
        url = super().get_email_confirmation_url(request, emailconfirmation)
        if ('next' in request.POST and
            url_has_allowed_host_and_scheme(
                request.POST['next'],
                allowed_hosts={request.get_host()})):
            return '{}?next={}'.format(url, quote(request.POST['next']))
        else:
            return url

    def send_mail(self, template_prefix, email, context):
        return AccountEmail.send(
            email,
            template_name=template_prefix,
            **context
        )

    def get_email_confirmation_redirect_url(self, request):
        if ('next' in request.GET and
            url_has_allowed_host_and_scheme(
                request.GET['next'],
                allowed_hosts={request.get_host()})):
            return request.GET['next']
        else:
            return super().get_email_confirmation_redirect_url(request)
