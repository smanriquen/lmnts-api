# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('M2M', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='characteristics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('characteristicType', models.CharField(max_length=140, blank=True)),
                ('value', models.CharField(max_length=140, blank=True)),
                ('timer', models.CharField(max_length=140, blank=True)),
                ('lastRead', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='machine',
            name='characteristics',
        ),
        migrations.RemoveField(
            model_name='machine',
            name='machinetype',
        ),
        migrations.AddField(
            model_name='machine',
            name='machineType',
            field=models.CharField(max_length=140, blank=True),
        ),
        migrations.AlterField(
            model_name='machine',
            name='MAC',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='machine',
            name='family',
            field=models.CharField(max_length=140, blank=True),
        ),
        migrations.AlterField(
            model_name='machine',
            name='serial',
            field=models.CharField(max_length=100, serialize=False, primary_key=True, blank=True),
        ),
        migrations.AlterField(
            model_name='machine',
            name='services',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='lecture',
        ),
        migrations.AddField(
            model_name='characteristics',
            name='parent',
            field=models.ForeignKey(related_name='characteristics', blank=True, to='M2M.machine'),
        ),
    ]
