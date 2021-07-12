from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from feedbacks.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
import feedbacks.translation

urlpatterns = [
    url(r'^support/$', feedback, name='feedback'),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
