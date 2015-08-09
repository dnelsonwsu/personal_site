# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0002_auto_20141227_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='created',
            field=models.DateTimeField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='updated',
            field=models.DateTimeField(null=True, editable=False),
        ),
    ]
