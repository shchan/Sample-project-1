from django.db import models
from django.contrib.postgres.fields import DateRangeField

from hotel.models import Room

class Availability(models.Model):
    room = models.ForeignKey(Room)
    period = DateRangeField()

    def __str__(self):
        return '%s %s - %s' % (self.room, self.period.lower, self.period.upper)

    class Meta:
        verbose_name_plural = 'availabilities'
