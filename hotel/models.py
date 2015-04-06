from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel)
    beds = models.IntegerField(default=1)

    def featured_image(self):
        featured = self.photos.first()
        return featured.image if featured else ""

    def featured_image_url(self):
        featured = self.photos.first()
        return featured.image.url if featured else ""

    def __str__(self):
        return '%s %s beds' % (self.hotel, self.beds)

def upload_path(instance, filename):
    return '%s/%s' % (instance._meta.model_name, filename)

class Photo(models.Model):
    image = models.ImageField(upload_to=upload_path)

    class Meta:
        abstract = True

class HotelPhoto(Photo):
    hotel = models.ForeignKey(Hotel, related_name="photos")

class RoomPhoto(Photo):
    room = models.ForeignKey(Room, related_name="photos")
