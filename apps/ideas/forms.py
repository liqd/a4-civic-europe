from django.forms import ModelForm
from django.utils.translation import ugettext as _

from .models.abstracts.applicant_section import AbstractApplicantSection
from .models.abstracts.collaboration_camp_section import \
    AbstractCollaborationCampSection
from .models.abstracts.community_section import AbstractCommunitySection
from .models.abstracts.finances_section import AbstractFinanceSection
from .models.abstracts.idea_section import AbstractIdeaSection
from .models.abstracts.impact_section import AbstractImpactSection
from .models.abstracts.partners_section import AbstractPartnersSection


class ApplicantSectionForm(ModelForm):
    section_name = _('Applicant Section')

    class Meta:
        model = AbstractApplicantSection
        exclude = []


class PartnersSectionForm(ModelForm):
    section_name = _('Partners')

    class Meta:
        model = AbstractPartnersSection
        exclude = []


class IdeaSectionForm(ModelForm):
    section_name = _('Idea details')

    class Meta:
        model = AbstractIdeaSection
        exclude = []


class ImpactSectionForm(ModelForm):
    section_name = _('Impact')

    class Meta:
        model = AbstractImpactSection
        exclude = []


class CollaborationCampSectionForm(ModelForm):
    section_name = _('Finances')

    class Meta:
        model = AbstractCollaborationCampSection
        exclude = []


class CommunitySectionForm(ModelForm):
    section_name = _('Community Information')

    class Meta:
        model = AbstractCommunitySection
        exclude = []


class FinanceSectionForm(ModelForm):
    section_name = _('Finances')

    class Meta:
        model = AbstractFinanceSection
        exclude = []
