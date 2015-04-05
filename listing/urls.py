from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    # e.g. /listing/
    url(r'^$', views.index),
    # e.g. /listing/1/
    url(r'^(?P<listing_id>[0-9]+)/$', views.detail, name='detail'),
]
