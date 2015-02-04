# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0005_auto_20150201_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='headshot',
            field=models.URLField(default=b'https://ivegotaproblemblog.files.wordpress.com/2012/07/386px-tux-g2-svg1.png'),
            preserve_default=True,
        ),
    ]
