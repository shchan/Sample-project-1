from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.DetailView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.BookingDetailView.as_view(), name='detail'),
]
