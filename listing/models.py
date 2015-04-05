from django.db import models
from django.contrib.postgres.fields import DateTimeRangeField

from hotel.models import Room

class Availability(models.Model):
    room = models.ForeignKey(Room)
    period = DateTimeRangeField()

    class Meta:
        verbose_name_plural = 'availabilities'
