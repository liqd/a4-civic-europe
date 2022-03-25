from django.urls import re_path

from . import models, views


def invite_urls(invite_model):
    view_name = invite_model.__name__.lower()

    return [
        re_path(
            r'^{}/(?P<invite_token>[-\w_]+)/$'.format(view_name),
            views.InviteDetailView.as_view(),
            name='{}-detail'.format(view_name)
        ),
        re_path(
            r'^{}/(?P<invite_token>[-\w_]+)/accept/$'.format(view_name),
            views.InviteUpdateView.as_view(),
            name='{}-update'.format(view_name)
        ),
    ]


urlpatterns = invite_urls(models.IdeaInvite)
