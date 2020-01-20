import os
from datetime import datetime

from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.forms.models import model_to_dict
from django.shortcuts import redirect
from django.utils.translation import ugettext as _
from django.views import generic
from formtools.wizard.views import SessionWizardView
from pytz import timezone
from rules.contrib.views import PermissionRequiredMixin

from adhocracy4.exports import mixins as export_mixins
from adhocracy4.exports import views as export_views
from adhocracy4.filters import views as filter_views
from adhocracy4.phases.models import Phase
from apps.wizards import mixins as wizard_mixins

from . import filters, forms, mixins
from .models import Idea


class IdeaExportView(PermissionRequiredMixin,

                     export_views.BaseExport,
                     export_mixins.ItemExportWithLinkMixin,
                     mixins.ExportMultiModelIdeaFieldsMixin,
                     export_mixins.ItemExportWithRatesMixin,
                     export_mixins.ItemExportWithCommentCountMixin,
                     export_mixins.ItemExportWithCommentsMixin,

                     # Both AbstractXlsxExportView and FilteredListView
                     # define `get()`. To ensure data is exported, the
                     # AbstractXlsxExportView class has to be defined first.
                     export_views.AbstractXlsxExportView,
                     filter_views.FilteredListView,
                     ):

    permission_required = 'civic_europe_ideas.export_idea'
    model = Idea
    filter_set = filters.IdeaFilterSet
    exclude = ['module', 'item_ptr', 'slug', 'idea_ptr',
               'idea_image', 'idea_sketch_archived']

    def get_base_filename(self):
        settings_time_zone = timezone(settings.TIME_ZONE)
        return 'download_%s' % (
            datetime.now(settings_time_zone).strftime('%Y%m%dT%H%M%S'))

    def get_queryset(self):
        queryset = super().get_queryset()\
            .annotate_comment_count()\
            .annotate_positive_rating_count()
        return queryset

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated

    def get_comment_count_data(self, item):
        item = item.idea
        return super().get_comment_count_data(item)

    def get_comments_data(self, item):
        item = item.idea
        return super().get_comments_data(item)

    def get_ratings_positive_data(self, item):
        item = item.idea
        return super().get_ratings_positive_data(item)

    def get_creator_data(self, item):
        return item.creator.email

    def get_created_data(self, item):
        return item.created.isoformat()

    def get_co_workers_data(self, item):
        co_workers = ', '.join(
            [co_worker.email for co_worker in item.idea.co_workers.all()]
        )
        return co_workers


class IdeaCreateWizard(PermissionRequiredMixin,
                       mixins.ModuleMixin,
                       wizard_mixins.CustomWizardMixin,
                       SessionWizardView):
    permission_required = 'civic_europe_ideas.add_idea'
    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, 'idea_images'))
    title = _('Idea')
    finish_section_text = _('As soon as you have submitted your application, '
                            'it will be published online in the idea space.')
    finish_section_btn = _('Submit your idea')

    @property
    def end_date(self):
        if (self.module.active_phase and
                self.module.active_phase.has_feature('crud', Idea)):
            settings_time_zone = timezone(settings.TIME_ZONE)
            end_date = self.module.active_phase.end_date
            return end_date.astimezone(settings_time_zone)\
                .strftime("%d %B %Y (%H:%M CET)")

    def get_form_kwargs(self, step=None):
        if step == '0':
            return {'end_date': self.end_date}
        return {}

    def done(self, form_list, **kwargs):
        special_fields = ['accept_conditions', 'co_workers_emails',
                          'confirm_publicity', 'confirm_idea_challenge_camp']

        data = self.get_all_cleaned_data()
        idea = Idea.objects.create(
            creator=self.request.user,
            module=self.module,
            **{
                field: value for field, value in data.items()
                if field not in special_fields
            }
        )

        for name, email in data['co_workers_emails']:
            idea.ideainvite_set.invite(
                self.request.user,
                email
            )

        return redirect(idea.get_absolute_url())

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated


class IdeaEditView(
    PermissionRequiredMixin,
    mixins.MultiFormEditMixin,
    SuccessMessageMixin,
    generic.UpdateView
):
    permission_required = 'civic_europe_ideas.change_idea'
    model = Idea
    template_name = 'civic_europe_ideas/idea_update_form.html'
    success_message = _('Idea Sketch saved')
    next_view = 'idea-update-form'
    title = _('Update Idea')

    form_classes = [
        forms.ApplicantSectionForm,
        forms.PartnersSectionForm,
        forms.IdeaSectionForm,
        forms.LocalDimensionSectionForm,
        forms.RoadToImpactSectionForm,
        forms.FinanceSectionForm,
        forms.NetworkAndCommunitySectionEditForm,
    ]

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated


class IdeaDetailView(generic.DetailView):
    display_type = 'idea'
    model = Idea
    queryset = Idea.objects.annotate_positive_rating_count()

    @property
    def idea_dict(self):
        return model_to_dict(self.object)

    def get_context_data(self, **kwargs):
        idea_list_1 = []
        idea_list_2 = []
        budget_list = []
        idea_list_1.append((_('Idea pitch'), self.object.idea_pitch))
        if self.object.idea_location_specify:
            idea_list_1.append((_('Where will your idea take place?'),
                                self.object.idea_location_specify))
        idea_list_1.append((_('Why does Europe need your idea?'),
                            self.object.challenge))
        idea_list_1.append((_('What is your impact?'), self.object.outcome))
        idea_list_1.append((_('How do you get there?'), self.object.plan))
        idea_list_1.append((_('What is your story?'), self.object.importance))
        idea_list_1.append((_('Who are you doing it for?'),
                            self.object.target_group))

        if self.object.reach_out:
            idea_list_2.append((_('What do you need from the Civic Europe '
                                'community?'), self.object.reach_out))

        partner_list = []
        if (self.object.partner_organisation_1_name
                or self.object.partner_organisation_1_website):
            partner_list.append((self.object.partner_organisation_1_name,
                                 self.object.partner_organisation_1_website,
                                 self.object.
                                 get_partner_organisation_1_country_display))
        if (self.object.partner_organisation_2_name
                or self.object.partner_organisation_2_website):
            partner_list.append((self.object.partner_organisation_2_name,
                                 self.object.partner_organisation_2_website,
                                 self.object.
                                 get_partner_organisation_2_country_display))
        if (self.object.partner_organisation_3_name
                or self.object.partner_organisation_3_website):
            partner_list.append((self.object.partner_organisation_3_name,
                                 self.object.partner_organisation_3_website,
                                 self.object.
                                 get_partner_organisation_3_country_display))

        context = super().get_context_data(**kwargs)
        context['idea_list_1'] = idea_list_1
        context['idea_list_2'] = idea_list_2
        context['budget_list'] = budget_list
        context['partner_list'] = partner_list
        return context


class IdeaListView(mixins.CtaPaginatorMixin, filter_views.FilteredListView):
    model = Idea
    paginator_class = None
    paginate_by = 9
    filter_set = filters.IdeaFilterSet

    @property
    def active_phase(self):
        return Phase.objects.active_phases().last()

    def get_queryset(self):
        queryset = super().get_queryset()\
            .annotate_comment_count()\
            .annotate_positive_rating_count()
        return queryset

    def filter_kwargs(self):
        default_kwargs = super().filter_kwargs()
        if self.active_phase:
            data = (self.active_phase.content().get_phase_filters(
                self.active_phase.module.project.pk).copy()
            )
            for key in default_kwargs['data']:
                data.setlist(key, [default_kwargs['data'][key]])
            default_kwargs['data'] = data
        return default_kwargs
