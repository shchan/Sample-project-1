# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields.ranges


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('period', django.contrib.postgres.fields.ranges.DateRangeField()),
                ('room', models.ForeignKey(to='hotel.Room')),
            ],
            options={
                'verbose_name_plural': 'availabilities',
            },
        ),
    ]
