# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='hotel',
        ),
        migrations.AlterModelOptions(
            name='availability',
            options={'verbose_name_plural': 'availabilities'},
        ),
        migrations.AlterField(
            model_name='availability',
            name='room',
            field=models.ForeignKey(to='hotel.Room'),
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
