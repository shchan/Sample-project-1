from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('listing.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^hotel/', include('hotel.urls')),
    url(r'^listing/', include('listing.urls', namespace="listing")),

    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
