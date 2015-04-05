from django.contrib import admin

from .models import (
    Availability,
    Hotel,
    Room,
)

admin.site.register(Availability)
admin.site.register(Hotel)
admin.site.register(Room)
