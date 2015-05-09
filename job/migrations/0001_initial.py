# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(help_text='Format should be : 650-111-2222', max_length=12)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HealthCareCompany',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oshpd_id', models.CharField(unique=True, max_length=60)),
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
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('phone_number', models.CharField(max_length=255, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=75, verbose_name='Email')),
                ('formerworker', models.BooleanField(default=False)),
                ('comments', models.TextField(verbose_name='Comments', blank=True)),
                ('contact_time', models.PositiveSmallIntegerField(default=0, verbose_name='Best Time To Talk', choices=[(0, '9:00 - 12:00'), (1, '12:00 - 13:00'), (2, '13:00 - 17:00'), (3, '18:00 - 21:00')])),
                ('application_date', models.DateTimeField(auto_now_add=True, verbose_name='Application Date')),
            ],
            options={
                'ordering': ['application_date'],
                'verbose_name': 'Job Application',
                'verbose_name_plural': 'Job Applications',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('publication_date', models.DateTimeField(null=True, verbose_name='Publication Date', blank=True)),
                ('expiration_date', models.DateTimeField(null=True, verbose_name='Expiration Date', blank=True)),
                ('published', models.BooleanField(default=True, verbose_name='Published')),
                ('title', models.CharField(max_length=255, verbose_name='Title', choices=[('RN', 'RN'), ('LVN', 'LVN'), ('CHHA', 'CHHA'), ('CNA', 'CNA'), ('CAREGIVER', 'CAREGIVER')])),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Order')),
            ],
            options={
                'ordering': ['order', '-creation_date'],
                'verbose_name': 'Job Position',
                'verbose_name_plural': 'Job Positions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'place',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='position',
            field=models.ForeignKey(related_name='applications', verbose_name='Position', to='job.JobPosition'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
