from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^create/idea/(?P<slug>[-\w_]+)/$',
            views.JourneyEntryCreateView.as_view(),
            name='journey-entry-create'),
    re_path(r'^(?P<pk>[-\w_]+)/edit/$',
            views.JourneyEntryUpdateView.as_view(),
            name='journey-entry-update'),
    re_path(r'^(?P<pk>[-\w_]+)/delete/$',
            views.JourneyEntryDeleteView.as_view(),
            name='journey-entry-delete'),
]
