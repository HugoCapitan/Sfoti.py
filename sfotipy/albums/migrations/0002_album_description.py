# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='description',
            field=models.CharField(default=b"<class 'artists.models.Artist'> compuso esto con mucho carino", max_length=255, editable=False),
            preserve_default=True,
        ),
    ]
