# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
        ('artists', '0002_auto_20141203_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='favorite_songs',
            field=models.ManyToManyField(related_name='is_favorite_of', to='tracks.Track', blank=True),
            preserve_default=True,
        ),
    ]
