# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_auto_20150401_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcarecompany',
            name='status_date',
            field=models.CharField(max_length=15),
            preserve_default=True,
        ),
    ]
