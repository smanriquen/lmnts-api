# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='device',
            fields=[
                ('reference', models.IntegerField(serialize=False, primary_key=True)),
                ('description', models.TextField(max_length=140)),
                ('command', models.TextField()),
            ],
        ),
    ]
