# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('is_public', models.BooleanField(verbose_name='public', default=True)),
                ('date_created', models.DateTimeField(verbose_name='date created')),
                ('date_update', models.DateTimeField(verbose_name='date updated')),
                ('owner', models.ForeignKey(related_name='bookmarks', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'verbose_name': 'bookmark',
                'verbose_name_plural': 'bookmarks',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='PublicBookMarkManager',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='bookmark',
            name='tags',
            field=models.ManyToManyField(blank=True, to='marcador.Tag'),
        ),
    ]
