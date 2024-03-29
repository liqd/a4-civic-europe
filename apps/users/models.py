from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models
from django.db.models import Q
from django.templatetags.static import static
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from easy_thumbnails.files import get_thumbnailer

from adhocracy4.images import fields
from apps.ideas.models import Idea

from . import USERNAME_INVALID_MESSAGE, USERNAME_REGEX


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    username = models.CharField(
        _('username'),
        max_length=75,
        unique=True,
        help_text=_(
            'Required. 60 characters or less. Letters, digits, spaces and '
            '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(
                USERNAME_REGEX, USERNAME_INVALID_MESSAGE, 'invalid')],
        error_messages={
            'unique': _('A user with that username already exists.')}
    )

    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'unique': _('A user with that email address already exists.')}
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.')
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.')
    )

    _avatar = fields.ConfiguredImageField(
        'avatar',
        upload_to='users/images',
        blank=True,
        verbose_name=_('Profile picture'),
        help_text=_('Please upload a picture in landscape format, at least '
                    '340x340 px. You can upload a .jpg, .png or .gif.')
    )

    date_joined = models.DateTimeField(
        editable=False,
        default=timezone.now
    )

    twitter_handle = models.CharField(
        blank=True,
        max_length=15,
        verbose_name=_('Twitter name'),
    )

    facebook_handle = models.CharField(
        blank=True,
        max_length=50,
        verbose_name=_('Facebook name'),
    )

    instagram_handle = models.CharField(
        blank=True,
        max_length=30,
        verbose_name=_('Instagram name'),
    )

    website = models.URLField(
        blank=True,
        verbose_name=_('Website'),
        help_text=_('Please add either https:// or http:// '
                    'at the beginning of your URL.')
    )

    get_notifications = models.BooleanField(
        verbose_name=_("my own ideas and ideas that I'm watching"),
        default=True
    )

    objects = auth_models.UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def avatar(self):
        if self._avatar:
            return self._avatar

    @property
    def fallback_avatar(self):
        number = self.pk % 3
        return static('images/avatar-{0:02d}.svg'.format(number))

    @property
    def is_innovator(self):
        return Idea.objects.filter(
            Q(creator=self) |
            Q(co_workers=self)
        ).count() > 0

    def avatar_or_fallback_url(self):
        if self._avatar:
            return get_thumbnailer(self._avatar)['avatar'].url
        else:
            return self.fallback_avatar

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        full_name = '%s <%s>' % (self.username, self.email)
        return full_name.strip()

    def signup(self, username, email, commit=True):
        """Update the fields required for sign-up."""
        self.username = username
        self.email = email
        if commit:
            self.save()

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.username)])
