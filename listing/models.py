from django.db import models
from django.contrib.postgres.fields import DateTimeRangeField

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

class Room(models.Model):
    hotel = models.ForeignKey(Hotel)
    beds = models.IntegerField(default=1)

class Availability(models.Model):
    room = models.ForeignKey(Room)
    period = DateTimeRangeField()

    class Meta:
        verbose_name_plural = 'availabilities'
