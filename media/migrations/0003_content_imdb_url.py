# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_auto_20150130_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='IMDB_url',
            field=models.URLField(default='null'),
            preserve_default=False,
        ),
    ]
