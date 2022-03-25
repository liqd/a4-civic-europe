from django.urls import path, re_path

from . import views
from .forms import (ApplicantSectionForm, FinanceSectionForm, FinishForm,
                    IdeaSectionForm, LocalDimensionSectionForm,
                    NetworkAndCommunitySectionForm, PartnersSectionForm,
                    RoadToImpactSectionForm)

urlpatterns = [
    re_path(r'create/module/(?P<slug>[-\w_]+)/$',
            views.IdeaCreateWizard.as_view(
                [ApplicantSectionForm, PartnersSectionForm,
                 IdeaSectionForm, LocalDimensionSectionForm,
                 RoadToImpactSectionForm, FinanceSectionForm,
                 NetworkAndCommunitySectionForm,
                 FinishForm]), name='idea-create'),
    re_path(r'^(?P<slug>[-\w_]+)/$',
            views.IdeaDetailView.as_view(), name='idea-detail'),
    re_path(r'^(?P<slug>[-\w_]+)/edit/$',
            views.IdeaEditView.as_view(), name='idea-update'),
    re_path(r'^(?P<slug>[-\w_]+)/edit/(?P<form_number>[\d]+)/$',
            views.IdeaEditView.as_view(), name='idea-update-form'),
    path('list/export/', views.IdeaExportView.as_view(),
         name='idea-export'),
    path('',
         views.IdeaListView.as_view(), name='idea-list')

]
