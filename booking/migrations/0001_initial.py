# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields.ranges


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_auto_20150519_0335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('period', django.contrib.postgres.fields.ranges.DateRangeField()),
                ('room', models.ForeignKey(to='hotel.Room')),
            ],
        ),
    ]
