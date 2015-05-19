# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import hotel.models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_hotelphoto_roomphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelphoto',
            name='image',
            field=models.ImageField(upload_to=hotel.models.upload_path),
        ),
        migrations.AlterField(
            model_name='roomphoto',
            name='image',
            field=models.ImageField(upload_to=hotel.models.upload_path),
        ),
    ]
