# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faces', '0002_face_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
