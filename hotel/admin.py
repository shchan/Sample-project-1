from django.contrib import admin

# Register your models here.
from .models import (
    Hotel,
    Room,
    HotelPhoto,
    RoomPhoto,
)

class HotelPhotoInline(admin.TabularInline):
    model = HotelPhoto

class HotelAdmin(admin.ModelAdmin):
    inlines = [
        HotelPhotoInline
    ]

class RoomPhotoInline(admin.TabularInline):
    model = RoomPhoto

class RoomAdmin(admin.ModelAdmin):
    inlines = [
        RoomPhotoInline
    ]

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(HotelPhoto)
admin.site.register(RoomPhoto)
