from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^hotel/', include('hotel.urls')),
    url(r'^listing/', include('listing.urls', namespace="listing")),
    url(r'^admin/', include(admin.site.urls)),
]
