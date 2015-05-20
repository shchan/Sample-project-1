from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$',
        login_required(views.DetailView.as_view())),
    url(r'^(?P<pk>[0-9]+)/$',
        login_required(views.BookingDetailView.as_view()),
        name='detail'),
]
