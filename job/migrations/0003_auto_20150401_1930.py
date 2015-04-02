# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_healthcarecompany'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcarecompany',
            name='latitude',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='healthcarecompany',
            name='longitude',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
