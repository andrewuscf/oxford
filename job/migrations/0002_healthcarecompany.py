# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthCareCompany',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oshpd_id', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=7)),
                ('county_code', models.CharField(max_length=50)),
                ('county_name', models.CharField(max_length=60)),
                ('status', models.CharField(max_length=20)),
                ('status_date', models.DateField()),
                ('license_type', models.CharField(max_length=150)),
                ('license_category', models.CharField(max_length=60)),
                ('link', models.URLField()),
                ('full_address', models.CharField(max_length=200, null=True, blank=True)),
                ('npi', models.CharField(max_length=150, null=True, blank=True)),
                ('cahsah', models.CharField(max_length=150, null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
    ]
