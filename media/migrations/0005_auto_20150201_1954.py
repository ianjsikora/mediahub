# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0004_person_tomato_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='roles',
            field=models.ManyToManyField(to='media.Character'),
            preserve_default=True,
        ),
    ]
