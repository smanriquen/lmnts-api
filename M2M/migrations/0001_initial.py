# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lecture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lecturetype', models.CharField(max_length=140)),
                ('value', models.CharField(max_length=140)),
                ('timer', models.TimeField()),
                ('lastread', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='machine',
            fields=[
                ('machinetype', models.CharField(max_length=140)),
                ('family', models.CharField(max_length=140)),
                ('serial', models.IntegerField(serialize=False, primary_key=True)),
                ('MAC', models.IntegerField()),
                ('characteristics', models.TextField()),
                ('services', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='lecture',
            name='parent',
            field=models.ForeignKey(to='M2M.machine'),
        ),
    ]
