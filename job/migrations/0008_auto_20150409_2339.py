# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_auto_20150409_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcarecompany',
            name='status_date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
