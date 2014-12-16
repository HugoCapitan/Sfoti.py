# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_album_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='description',
        ),
    ]
