from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from landing import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^country/(?P<country_id>[0-9a-f-]+)/$', views.country, name='country'),
    url(r'^country/', views.country, name='country'),
    url(r'^countries/$', views.countriess, name='countries'),
    url(r'^accounts/login/$', views.user_login, name="login"),
    url(r'^zavod/$', views.assortiment, name='assortiment'),
    url(r'^prana_(?P<country_id>[0-9a-f-]+)/(?P<prana_id>\w+)/$', views.models, name='models'),
    url(r'^prana_(?P<country_id>[0-9a-f-]+)/(?P<prana_id>\w+)/(?P<revision_id>\w+)/$', views.revisions, name='revisions'),
    url(r'^assort/', views.models, name='models'),
    url(r'^qr-codes/$', views.qr, name='qr'),
    url(r'app/$', views.download, name="download"),
    url(r'^(?P<extra_id>\w+)/$', views.extra_country, name='extra_country'),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
