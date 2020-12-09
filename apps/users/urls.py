from django.conf.urls import url

from . import USERNAME_REGEX, views

urlpatterns = [
    url(
        '^profile/(?P<username>{})/$'.format(USERNAME_REGEX[1:-1]),
        views.ProfileView.as_view(),
        name='profile',
    ),
    url(
        '^accounts/edit/$',
        views.EditProfileView.as_view(),
        name='edit_profile',
    ),
    url(
        '^accounts/notifications/$',
        views.NotificationsView.as_view(),
        name='notifications',
    ),
]
