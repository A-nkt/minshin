from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
import ans_upload.views as ans_upload
from django.urls import path

from wagtail.contrib.sitemaps.views import sitemap

urlpatterns = [
    path('',include('ans_upload.urls')),#ans_upload用のurl
    url(r'^django-admin/', admin.site.urls),#Djangoの管理画面
    url('^sitemap\.xml$', sitemap),#サイトマップ
    url(r'^admin/', include(wagtailadmin_urls)),#wagtailの管理画面
    url(r'^documents/', include(wagtaildocs_urls)),#存在しない模様(2020.08.16)
    url(r'^search/$', search_views.search, name='search'),#検索
]

if settings.DEBUG:#DEBUGの時
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r"", include(wagtail_urls)),#これはこのページの最後になければなりません。

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r"^pages/", include(wagtail_urls)),
]
