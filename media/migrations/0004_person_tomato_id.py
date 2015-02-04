# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_content_imdb_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='tomato_id',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
