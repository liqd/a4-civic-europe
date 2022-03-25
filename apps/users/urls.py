from django.urls import path, re_path

from . import USERNAME_REGEX, views

urlpatterns = [
    re_path(
        '^profile/(?P<username>{})/$'.format(USERNAME_REGEX[1:-1]),
        views.ProfileView.as_view(),
        name='profile',
    ),
    path(
        'accounts/edit/',
        views.EditProfileView.as_view(),
        name='edit_profile',
    ),
    path(
        'accounts/notifications/',
        views.NotificationsView.as_view(),
        name='notifications',
    ),
]
