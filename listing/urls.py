from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    # e.g. /listing/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^s/', views.SearchView.as_view(), name='search'),
    # e.g. /listing/1/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
