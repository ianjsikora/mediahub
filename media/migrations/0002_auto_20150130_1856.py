# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='ratings_audience',
            new_name='rating_tomato_a',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='ratings_critics',
            new_name='rating_tomato_c',
        ),
        migrations.AddField(
            model_name='content',
            name='IMDb_id',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='content',
            name='rating_imdb',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
    ]
