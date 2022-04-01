from allauth import urls as allauth_urls
from ckeditor_uploader import views as ck_views
from django.conf import settings
from django.conf.urls import i18n
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from django.views.i18n import JavaScriptCatalog
from rest_framework import routers
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.sitemaps import views as wagtail_sitemap_views
from wagtail.contrib.sitemaps.sitemap_generator import \
    Sitemap as WagtailSitemap
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from adhocracy4.api import routers as a4routers
from adhocracy4.comments.api import CommentViewSet
from adhocracy4.ratings.api import RatingViewSet
from adhocracy4.reports.api import ReportViewSet
from apps.contrib.sitemaps.adhocracy4_sitemap import Adhocracy4Sitemap
from apps.contrib.sitemaps.static_sitemap import StaticSitemap
from apps.follows.api import FollowViewSet
from apps.ideas import urls as idea_urls
from apps.invites import urls as invite_urls
from apps.journeys import urls as journey_urls
from apps.users import urls as user_urls

js_info_dict = {
    'packages': ('adhocracy4.comments',),
}

router = routers.DefaultRouter()
router.register(r'reports', ReportViewSet, basename='reports')
router.register(r'follows', FollowViewSet, basename='follows')

ct_router = a4routers.ContentTypeDefaultRouter()
ct_router.register(r'comments', CommentViewSet, basename='comments')
ct_router.register(r'ratings', RatingViewSet, basename='ratings')

sitemaps = {
    'adhocracy4': Adhocracy4Sitemap,
    'wagtail': WagtailSitemap,
    'static': StaticSitemap
}

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('api/', include(router.urls)),
    path('api/', include(ct_router.urls)),
    path('upload/',
         login_required(ck_views.upload), name='ckeditor_upload'),
    path('browse/',
         never_cache(login_required(ck_views.browse)), name='ckeditor_browse'),
]

urlpatterns += [
    path('accounts/', include(allauth_urls)),
    path('', include(user_urls)),
    path('ideas/', include(idea_urls)),
    path('invites/', include(invite_urls)),
    path('journeys/', include(journey_urls)),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('i18n/', include(i18n)),

    re_path(r'^sitemap\.xml$', wagtail_sitemap_views.index,
            {'sitemaps': sitemaps, 'sitemap_url_name': 'sitemaps'}),
    re_path(r'^sitemap-(?P<section>.+)\.xml$', wagtail_sitemap_views.sitemap,
            {'sitemaps': sitemaps}, name='sitemaps'),
    re_path(r'^robots\.txt$', TemplateView.as_view(
            template_name='robots.txt',
            content_type="text/plain"), name="robots_file"),

    path('', include(wagtail_urls))
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    try:
        import debug_toolbar
    except ImportError:
        pass
    else:
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
