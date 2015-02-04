# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tomato_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(default=b'movie', max_length=6, choices=[(b'series', b'TV Series'), (b'movie', b'Movie')])),
                ('release_date', models.DateField()),
                ('runtime', models.IntegerField()),
                ('rating', models.CharField(max_length=10)),
                ('synopsis', models.TextField()),
                ('ratings_critics', models.IntegerField()),
                ('ratings_audience', models.IntegerField()),
                ('poster', models.URLField()),
                ('tomato_id', models.IntegerField()),
                ('cast', models.ManyToManyField(to='media.Character')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(default=b'actor', max_length=10, choices=[(b'director', b'Director'), (b'writer', b'Writer'), (b'actor', b'Actor')])),
                ('birthday', models.DateField(null=True)),
                ('headshot', models.URLField(null=True)),
                ('roles', models.ManyToManyField(to='media.Content')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='content',
            name='genre',
            field=models.ManyToManyField(to='media.Genre'),
            preserve_default=True,
        ),
    ]
