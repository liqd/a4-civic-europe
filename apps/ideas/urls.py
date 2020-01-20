from django.conf.urls import url

from . import views
from .forms import (ApplicantSectionForm, FinanceSectionForm, FinishForm,
                    IdeaSectionForm, LocalDimensionSectionForm,
                    NetworkAndCommunitySectionForm, PartnersSectionForm,
                    RoadToImpactSectionForm)

urlpatterns = [
    url(r'create/module/(?P<slug>[-\w_]+)/$',
        views.IdeaCreateWizard.as_view(
            [ApplicantSectionForm, PartnersSectionForm,
             IdeaSectionForm, LocalDimensionSectionForm,
             RoadToImpactSectionForm, FinanceSectionForm,
             NetworkAndCommunitySectionForm,
             FinishForm]), name='idea-create'),
    url(r'^(?P<slug>[-\w_]+)/$',
        views.IdeaDetailView.as_view(), name='idea-detail'),
    url(r'^(?P<slug>[-\w_]+)/edit/$',
        views.IdeaEditView.as_view(), name='idea-update'),
    url(r'^(?P<slug>[-\w_]+)/edit/(?P<form_number>[\d]+)/$',
        views.IdeaEditView.as_view(), name='idea-update-form'),
    url(r'list/export/$', views.IdeaExportView.as_view(),
        name='idea-export'),
    url(r'^$',
        views.IdeaListView.as_view(), name='idea-list')

]
