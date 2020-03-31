from itertools import chain
from zlib import adler32

import crispy_forms as crisp
from django import forms
from django.core.exceptions import ValidationError
from django.templatetags.static import static
from django.utils.translation import ugettext_lazy as _

from cms.contrib import helpers

from .models import Idea
from .models.sections import finances_section
from .models.sections.applicant_section import ApplicantSection
from .models.sections.idea_section import IdeaSection
from .models.sections.local_dimension_section import LocalDimensionSection
from .models.sections.network_community_section import NetworkSection
from .models.sections.partners_section import PartnersSection
from .models.sections.road_to_impact_section import RoadToImpactSection

CONFIRM_PUBLICITY_LABEL = _('I hereby confirm and agree that '
                            'my idea will be public once published. '
                            'I confirm that I have the right to share '
                            'the idea and the visual material '
                            'used.')
ACCEPT_CONDITIONS_LABEL = _('I hereby agree to the {}terms'
                            ' of use{} of the Civic'
                            ' Europe idea challenge.')

COWORKERS_TITLE = _('Please add your team members here.')
COWORKERS_HELP = _('Here you can insert the email addresses of '
                   'up to 5 team members. They will receive an email '
                   'inviting them to register on the Civic '
                   'Europe website. After registering they '
                   'will appear with their user name on your idea '
                   'page and will be able to edit your idea. ')

COWORKERS_EDIT_TITLE = _('Your team members')


class BaseForm(forms.ModelForm):
    do_not_call_in_templates = True  # important when reading section name

    @property
    def helper(self):
        helper = crisp.helper.FormHelper(self)
        helper.form_tag = False
        return helper


class CoWorkersEmailsFormMixin:
    def clean_co_workers_emails(self):
        from email.utils import getaddresses
        import re

        value = self.cleaned_data['co_workers_emails'].strip(' ,')
        addresses = getaddresses([value])
        valid_addresses = []
        errors = []

        for name, address in addresses:
            if not re.match(r'^.+@[^@]+', address):
                errors.append(
                    ValidationError('{msg} ({addr})'.format(
                        msg=_('Invalid email address'),
                        addr=address
                    ))
                )

            if address in valid_addresses:
                errors.append(
                    ValidationError('{msg} ({addr})'.format(
                        msg=_('Duplicate email address'),
                        addr=address
                    ))
                )
            else:
                valid_addresses.append(address)

        if errors:
            raise ValidationError(errors)

        return addresses


class ApplicantSectionForm(BaseForm):
    section_name = _('About You')

    class Meta:
        model = ApplicantSection
        fields = [
            'first_name',
            'last_name',
            'lead_organisation_name',
            'lead_organisation_status',
            'lead_organisation_details',
            'lead_organisation_website',
            'lead_organisation_country',
            'lead_organisation_city',
            'contact_email',
            'year_of_registration'
        ]

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('lead_organisation_status')
        details = cleaned_data.get(
            'lead_organisation_details')
        if status and status == 'OT':
            if not details:
                self.add_error('lead_organisation_details',
                               ("You selected 'other' as "
                                "organisation status. "
                                "Please provide more information "
                                "about your current status."))

    def __init__(self, *args, **kwargs):
        if 'end_date' in kwargs:
            self.end_date = kwargs.pop('end_date')
        else:
            self.end_date = None
        super().__init__(*args, **kwargs)
        if self.end_date:
            self.section_description = _('Applications may be submitted, '
                                         'in English only, until {}. '
                                         'After publishing, '
                                         'you can continue to edit '
                                         'all the fields '
                                         'of your application right up to {}.'
                                         .format(self.end_date, self.end_date))


class PartnersSectionForm(BaseForm):
    section_name = _('Partners')
    section_description_header = _('Please share the names '
                                   'of your partner organisations here.')

    section_description = _('If you do not have any partner '
                            'organisations, leave the fields empty. '
                            'You can update these fields any time '
                            'before the application deadline.')
    accordions = [
        _('Partner Organisation 1'),
        _('Partner Organisation 2'),
        _('Partner Organisation 3'),
    ]

    class Meta:
        model = PartnersSection
        fields = list(
            chain.from_iterable((
                'partner_organisation_{}_name'.format(index),
                'partner_organisation_{}_website'.format(index),
                'partner_organisation_{}_country'.format(index)
            ) for index in range(1, 4))
        )
        fields.append('partners_more_info')

    @property
    def helper(self):
        helper = super().helper
        helper.render_unmentioned_fields = True
        helper.layout = crisp.bootstrap.Accordion(
            *[
                crisp.bootstrap.AccordionGroup(
                    heading,
                    'partner_organisation_{}_name'.format(index),
                    'partner_organisation_{}_website'.format(index),
                    'partner_organisation_{}_country'.format(index)
                ) for index, heading in enumerate(self.accordions, 1)
            ]
        )
        return helper


class IdeaSectionForm(BaseForm):
    section_name = _('Idea')

    class Meta:
        model = IdeaSection
        fields = [
            'title',
            'subtitle',
            'pitch',
            'image',
            'topics',
            'topics_other'
        ]


class LocalDimensionSectionForm(BaseForm):
    section_name = _('Local Dimension')

    class Meta:
        model = LocalDimensionSection
        fields = [
            'location',
            'challenge',
            'impact',
            'target_group',
            'local_embedding',
            'uniqueness'
        ]


class RoadToImpactSectionForm(BaseForm):
    section_name = _('Road to impact & Motivation')

    class Meta:
        model = RoadToImpactSection
        fields = [
            'plan',
            'reach_out',
            'results',
            'sustainability',
            'contribution',
            'knowledge',
            'motivation'
        ]


class FinanceSectionForm(BaseForm):
    section_name = _('Finances')

    budget_requested = forms.IntegerField(
        max_value=50000,
        min_value=0,
        help_text=finances_section.BUDGET_REQUESTED_HELP
    )
    total_budget = forms.IntegerField(
        min_value=0,
        help_text=finances_section.TOTAL_BUDGET_HELP
    )

    class Meta:
        model = finances_section.FinancesSection
        fields = [
            'total_budget',
            'budget_requested',
            'major_expenses',
            'duration'
        ]

    def clean(self):
        cleaned_data = super().clean()
        budget_requested = cleaned_data.get('budget_requested')
        total_budget = cleaned_data.get('total_budget')

        if budget_requested and total_budget:
            if budget_requested > total_budget:
                self.add_error('__all__', _("The requested budget can't be "
                                            "higher than the total budget"))


class NetworkAndCommunitySectionForm(CoWorkersEmailsFormMixin, BaseForm):
    section_name = _('Network & Community')
    co_workers_emails = forms.CharField(
        required=False,
        help_text=COWORKERS_HELP,
        label=COWORKERS_TITLE)
    confirm_publicity = forms.BooleanField(label=CONFIRM_PUBLICITY_LABEL)
    accept_conditions = forms.BooleanField(label='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['accept_conditions'].label = helpers.add_link_to_helptext(
            self.fields['accept_conditions'].label, "terms_of_use_page",
            ACCEPT_CONDITIONS_LABEL)

    class Meta:
        model = NetworkSection
        fields = [
            'network',
            'co_workers_emails',
            'feedback',
            'accept_conditions'
        ]

    def clean_co_workers_emails(self):
        addresses = super().clean_co_workers_emails()

        if len(addresses) > 5:
            raise ValidationError(_('Maximum 5 team members allowed'))

        return addresses


class NetworkAndCommunitySectionEditForm(CoWorkersEmailsFormMixin, BaseForm):
    section_name = _('Network & Community')
    co_workers_emails = forms.CharField(
        required=False,
        help_text=COWORKERS_HELP,
        label=COWORKERS_TITLE)

    class Meta:
        model = Idea
        fields = [
            'network',
            'co_workers_emails',
            'feedback',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance:
            invites = self.instance.ideainvite_set.all()
            co_workers = self.instance.co_workers.all()
            if invites or co_workers:
                self.fields['co_workers'] = forms.MultipleChoiceField(
                    required=False,
                    label=COWORKERS_EDIT_TITLE,
                    choices=[
                        (
                            'c:' + c.username,
                            {
                                'username': c.username,
                                'avatar': c.avatar_or_fallback_url,
                                'cta_checked': _('remove'),
                                'cta_unchecked': _('will be removed on save')
                            }
                        ) for c in co_workers
                    ] + [
                        (
                            'i:' + i.email,
                            {
                                'username': i.email,
                                'avatar': self.fallback_avatar(i.email),
                                'detail': _('Invitation pending'),
                                'cta_checked': _('remove'),
                                'cta_unchecked': _('will be removed on save')
                            }
                        ) for i in invites
                    ],
                    initial=['c:' + c.username for c in co_workers] +
                            ['i:' + i.email for i in invites],
                    widget=forms.CheckboxSelectMultiple
                )
                self.fields.move_to_end('co_workers', last=False)

            self.fields.move_to_end('co_workers_emails', last=False)

    @property
    def helper(self):
        helper = super().helper
        helper['co_workers'].wrap(
            crisp.layout.Field,
            template="bootstrap3/user_checkboxselectmultiple_field.html",
        )
        return helper

    def fallback_avatar(self, email):
        number = adler32(bytes(email, 'UTF-8')) % 3
        return static('images/avatar-{0:02d}.svg'.format(number))

    def clean(self):
        super().clean()

        addresses = self.cleaned_data.get('co_workers_emails', [])
        invites = []
        co_workers = []
        for entry in self.cleaned_data.get('co_workers', []):
            if entry[:2] == 'c:':
                co_workers.append(entry[2:])
            else:
                invites.append(entry[2:])
        self.cleaned_data['invites'] = invites
        self.cleaned_data['co_workers'] = co_workers

        duplicate_errors = []
        for (name, address) in addresses:
            if address in invites:
                error = ValidationError({
                    'co_workers_emails': _(
                        'You already invited {email}'
                    ).format(email=address)
                })
                duplicate_errors.append(error)
        if duplicate_errors:
            raise ValidationError(duplicate_errors)

        co_worker_count = sum([
            len(addresses),
            len(invites),
            len(co_workers),
        ])

        if co_worker_count > 5:
            raise ValidationError(_('Maximum 5 team members allowed'))

    def save(self, commit=True):
        """
        Deletes invites and co-workers and adds new invites of instance.
        There is a little hack here, it uses the idea creator and not the
        current user as creator for the invites. Therefor no user needs to
        passed and it can be used in the edit view, just as all other forms.
        """
        super().save(commit)

        co_workers = self.instance.co_workers.exclude(
            username__in=self.cleaned_data.get('co_workers', [])
        )
        self.instance.co_workers.remove(*co_workers)

        self.instance.ideainvite_set.exclude(
            email__in=self.cleaned_data.get('invites', [])
        ).delete()

        if 'co_workers_emails' in self.cleaned_data:
            for name, email in self.cleaned_data['co_workers_emails']:
                self.instance.ideainvite_set.invite(
                    self.instance.creator,
                    email
                )

        return self.instance


class FinishForm(forms.Form):
    section_name = _('Submit and publish')

    class Meta:
        model = Idea
        exclude = [
            'co_workers_emails', 'creator', 'module'
        ]

    @property
    def helper(self):
        helper = crisp.helper.FormHelper()
        helper.form_tag = False
        return helper
