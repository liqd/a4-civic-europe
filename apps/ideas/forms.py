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
from .models.sections.partners_section import (CO_WORKERS_HELP,
                                               CO_WORKERS_LABEL,
                                               PartnersSection)
from .models.sections.road_to_impact_section import RoadToImpactSection

CONFIRM_PUBLICITY_LABEL = _('I hereby confirm and agree that '
                            'my idea will be public once published. '
                            'I confirm that I have the right to share '
                            'the idea and the visual material '
                            'used.')
ACCEPT_CONDITIONS_LABEL = _('I hereby agree to the {}terms'
                            ' of use{} of the Civic'
                            ' Europe idea challenge.')

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
        import re
        from email.utils import getaddresses

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

    section_description = _('Your first and last name will be '
                            'published together with the application.')

    class Meta:
        model = ApplicantSection
        fields = [
            'first_name',
            'last_name',
            'lead_organisation_name',
            'lead_organisation_status',
            'clarification_legal_status',
            'lead_organisation_details',
            'lead_organisation_website',
            'lead_organisation_country',
            'lead_organisation_location_name',
            'lead_organisation_location',
            'contact_email',
            'year_of_registration'
        ]
        widgets = {
            'year_of_registration': forms.TextInput(attrs={'maxlength': 20})
        }

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('lead_organisation_status')
        details = cleaned_data.get(
            'lead_organisation_details')
        if status and status == 'OT':
            if not details:
                self.add_error('lead_organisation_details',
                               ("You selected 'other' as "
                                "organization status. "
                                "Please provide more information "
                                "about your current status."))

    def __init__(self, *args, **kwargs):
        if 'end_date' in kwargs:
            self.end_date = kwargs.pop('end_date')
        else:
            self.end_date = None
        super().__init__(*args, **kwargs)
        if self.end_date:
            self.section_description = _('Deadline for the submission '
                                         'of project ideas is {}. '
                                         'If you submit your idea '
                                         'before the deadline, you '
                                         'will still be able to edit your '
                                         'application until this date. '
                                         'Please note that only applications'
                                         ' in English language will be '
                                         'considered.'
                                         .format(self.end_date))


class PartnersSectionForm(CoWorkersEmailsFormMixin, BaseForm):
    section_name = _('Partners')
    section_description_header = _('Please share information about '
                                   'your partner organizations here.')

    section_description = _('If you do not have any partner '
                            'organizations, leave the fields empty. '
                            'You can update these fields any time '
                            'before the application deadline. The '
                            'names of your partner organizations '
                            'and their online presence will be '
                            'published in the idea space.')
    accordions = [
        _('Partner Organization 1'),
        _('Partner Organization 2'),
        _('Partner Organization 3'),
    ]
    co_workers_emails = forms.CharField(
        required=False,
        help_text=CO_WORKERS_HELP,
        label=CO_WORKERS_LABEL)

    class Meta:
        model = PartnersSection
        fields = list(
            chain.from_iterable((
                'partner_organisation_{}_name'.format(index),
                'partner_organisation_{}_website'.format(index),
                'partner_organisation_{}_country'.format(index),
                'partner_organisation_{}_location_name'.format(index),
                'partner_organisation_{}_location'.format(index),
                'partner_organisation_{}_details'.format(index),
                'partner_organisation_{}_role'.format(index)
            ) for index in range(1, 4))
        )
        fields.append('partners_more_info')
        fields.append('co_workers_emails')

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
                    'partner_organisation_{}_country'.format(index),
                    'partner_organisation_{}_location_name'.format(index),
                    'partner_organisation_{}_location'.format(index),
                    'partner_organisation_{}_details'.format(index),
                    'partner_organisation_{}_role'.format(index)
                ) for index, heading in enumerate(self.accordions, 1)
            ]
        )
        return helper

    def clean_co_workers_emails(self):
        addresses = super().clean_co_workers_emails()

        if len(addresses) > 5:
            raise ValidationError(_('Maximum 5 team members allowed'))

        return addresses


class PartnersSectionEditForm(CoWorkersEmailsFormMixin, BaseForm):
    section_name = _('Partners')
    section_description_header = _('Please share information about '
                                   'your partner organizations here.')

    section_description = _('If you do not have any partner '
                            'organizations, leave the fields empty. '
                            'You can update these fields any time '
                            'before the application deadline. The '
                            'names of your partner organizations '
                            'and their online presence will be '
                            'published in the idea space.')
    accordions = [
        _('Partner Organization 1'),
        _('Partner Organization 2'),
        _('Partner Organization 3'),
    ]
    co_workers_emails = forms.CharField(
        required=False,
        help_text=CO_WORKERS_HELP,
        label=CO_WORKERS_LABEL)

    class Meta:
        model = PartnersSection
        fields = list(
            chain.from_iterable((
                'partner_organisation_{}_name'.format(index),
                'partner_organisation_{}_website'.format(index),
                'partner_organisation_{}_country'.format(index),
                'partner_organisation_{}_location_name'.format(index),
                'partner_organisation_{}_location'.format(index),
                'partner_organisation_{}_details'.format(index),
                'partner_organisation_{}_role'.format(index)
            ) for index in range(1, 4))
        )
        fields.append('partners_more_info')
        fields.append('co_workers_emails')

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

    @property
    def helper(self):
        helper = super().helper
        helper.render_unmentioned_fields = True

        helper.layout = crisp.layout.Layout(
            crisp.bootstrap.Accordion(
                *[
                    crisp.bootstrap.AccordionGroup(
                        heading,
                        'partner_organisation_{}_name'.format(index),
                        'partner_organisation_{}_website'.format(index),
                        'partner_organisation_{}_country'.format(index),
                        'partner_organisation_{}_location_name'.format(index),
                        'partner_organisation_{}_location'.format(index),
                        'partner_organisation_{}_details'.format(index),
                        'partner_organisation_{}_role'.format(index)
                    ) for index, heading in enumerate(self.accordions, 1)
                ]
            ),
            'partners_more_info',
            'co_workers_emails'
        )
        if 'co_workers' in self.fields:
            helper.layout.append(
                crisp.layout.Field(
                    'co_workers',
                    template="bootstrap3/"
                             "user_checkboxselectmultiple_field.html")
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


class IdeaSectionForm(BaseForm):
    section_name = _('Idea')

    class Meta:
        model = IdeaSection
        fields = [
            'title',
            'subtitle',
            'pitch',
            'image',
            'country_of_implementation',
            'field_of_action',
            'field_of_action_other'
        ]


class LocalDimensionSectionForm(BaseForm):
    section_name = _('Local Dimension')

    class Meta:
        model = LocalDimensionSection
        fields = [
            'location',
            'location_details',
            'location_details_mixed',
            'cohesion',
            'challenge',
            'target_group',
            'local_embedding',
            'perspective_and_dialog'
        ]

        widgets = {
            'location_details': forms.RadioSelect()
        }


class RoadToImpactSectionForm(BaseForm):
    section_name = _('Road to impact & Motivation')

    class Meta:
        model = RoadToImpactSection
        fields = [
            'plan',
            'reach_out',
            'results',
            'impact',
            'sustainability',
            'motivation'
        ]


class FinanceSectionForm(BaseForm):
    section_name = _('Finances')

    class Meta:
        model = finances_section.FinancesSection
        fields = [
            'total_budget',
            'budget_requested',
            'major_expenses',
            'duration'
        ]
        widgets = {
            'total_budget': forms.TextInput(attrs={'maxlength': 20}),
            'budget_requested': forms.TextInput(attrs={'maxlength': 20}),
            'duration': forms.TextInput(attrs={'maxlength': 20})
        }

    def clean(self):
        cleaned_data = super().clean()
        budget_requested = cleaned_data.get('budget_requested')
        total_budget = cleaned_data.get('total_budget')

        if budget_requested and total_budget:
            if budget_requested > total_budget:
                self.add_error('__all__', _("The requested budget can't be "
                                            "higher than the total budget"))


class NetworkAndCommunitySectionForm(BaseForm):
    section_name = _('Network & Community')
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
            'feedback',
            'accept_conditions'
        ]


class NetworkAndCommunitySectionEditForm(BaseForm):
    section_name = _('Network & Community')

    class Meta:
        model = Idea
        fields = [
            'network',
            'feedback',
        ]


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
