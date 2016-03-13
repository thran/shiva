# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import faces.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=255)),
                ('who', models.CharField(max_length=255)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Jm\xe9no')),
                ('alternatives', models.CharField(max_length=255, null=True, verbose_name='Alternativn\xed jm\xe9na, odd\u011blen\xe1 st\u0159edn\xedkem', blank=True)),
                ('hint', models.CharField(max_length=255, null=True, verbose_name='N\xe1pov\u011bda', blank=True)),
                ('photo', models.ImageField(upload_to=faces.models.update_filename)),
                ('photo_thumb', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Guess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=255)),
                ('who', models.CharField(max_length=255)),
                ('correct', models.BooleanField()),
                ('face', models.ForeignKey(to='faces.Face')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
