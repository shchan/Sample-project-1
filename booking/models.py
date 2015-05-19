from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import DateRangeField

from hotel.models import Room

# Create your models here.

class Booking(models.Model):
    made_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    room = models.ForeignKey(Room)
    period = DateRangeField()

    def __str__(self):
        return '%s %s - %s' % (self.room, self.period.lower, self.period.upper)
