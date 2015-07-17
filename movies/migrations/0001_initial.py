# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField(null=True, blank=True)),
                ('watch_date', models.DateField(default=b'1900-01-01')),
                ('imdb_link', models.URLField(null=True, blank=True)),
            ],
        ),
    ]
