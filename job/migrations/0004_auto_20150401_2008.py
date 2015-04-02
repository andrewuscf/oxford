# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_auto_20150401_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcarecompany',
            name='oshpd_id',
            field=models.CharField(unique=True, max_length=60),
            preserve_default=True,
        ),
    ]