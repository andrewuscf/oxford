from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from local_settings import GOOGLE_API_KEY
from managers import PublishableModelManager
from constants import *
from django.db import models
from django.utils.translation import ugettext_lazy as _
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import GoogleV3


class Worker(AbstractUser):
    phone = models.CharField(max_length=12, help_text="Format should be : 650-111-2222")


class PublishableModel(models.Model):
    creation_date = models.DateTimeField(_("Created"), auto_now_add=True)
    modification_date = models.DateTimeField(_("Modified"), auto_now=True)
    publication_date = models.DateTimeField(_("Publication Date"), blank=True, null=True)
    expiration_date = models.DateTimeField(_("Expiration Date"), blank=True, null=True)
    published = models.BooleanField(_("Published"), default=True)

    admin_objects = models.Manager()
    objects = PublishableModelManager()

    class Meta:
        abstract = True
        verbose_name = _("Publishable Model")
        verbose_name_plural = _("Publishable Models")

    def __unicode__(self):
        return u"Publishable Model"


class JobPosition(PublishableModel):
    RN = 'RN'
    LVN = 'LVN'
    CHHA = 'CHHA'
    CNA = 'CNA'
    CAREGIVER = 'CAREGIVER'
    JOB_TITLES = (
        (RN, 'RN'),
        (LVN, 'LVN'),
        (CHHA, 'CHHA'),
        (CNA, 'CNA'),
        (CAREGIVER, 'CAREGIVER'),
    )
    title = models.CharField(_("Title"), max_length=255, choices=JOB_TITLES)
    description = models.TextField(_("Description"), blank=True)
    order = models.PositiveSmallIntegerField(_("Order"), default=0)

    class Meta:
        verbose_name = _("Job Position")
        verbose_name_plural = _("Job Positions")
        ordering = ["order", "-creation_date"]

    def __unicode__(self):
        return self.title


class JobApplication(models.Model):

    position = models.ForeignKey(JobPosition, verbose_name=_("Position"), related_name="applications")
    user = models.ForeignKey(Worker)
    address = models.CharField(_("Address"), max_length=255)
    phone_number = models.CharField(_("Phone Number"), max_length=255)
    email = models.EmailField(_("Email"))
    formerworker = models.BooleanField(default=False)
    comments = models.TextField(_("Comments"), blank=True)
    contact_time = models.PositiveSmallIntegerField(_("Best Time To Talk"), choices=APPLICATION_CONTACT_TIME_CHOICES,
                                                    default=APPLICATION_CONTACT_TIME_MORNING)
    application_date = models.DateTimeField(_("Application Date"), auto_now_add=True)

    @property
    def full_name(self):
        return self.user

    class Meta:
        verbose_name = _("Job Application")
        verbose_name_plural = _("Job Applications")
        ordering = ["application_date"]

    def __unicode__(self):
        return self.full_name


class Place(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def coordinates(self):
        if self.location:
            geocoder = GoogleV3()
            address = self.location
            try:
                location, (latitude, longitude) = geocoder.geocode(address)
            except GeocoderTimedOut:
                location = address

            return location, latitude, longitude

            self.latitude = latitude
            self.longitude = longitude
            self.save()

    class Meta:
        db_table = 'place'

    def __unicode__(self):
        return u'{}'.format(self.title)


class HealthCareCompany(models.Model):
    oshpd_id = models.CharField(max_length=60, unique=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=7)
    county_code = models.CharField(max_length=50)
    county_name = models.CharField(max_length=60)
    status = models.CharField(max_length=20)
    status_date = models.DateField()
    license_type = models.CharField(max_length=150)
    license_category = models.CharField(max_length=60)
    link = models.URLField()
    full_address = models.CharField(max_length=200, blank=True, null=True)
    npi = models.CharField(max_length=150, null=True, blank=True)
    cahsah = models.CharField(max_length=150, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return "%s, %s" % (self.name, self.full_address)

    class Meta:
        ordering = ['name']

    # def location(self):
    #     if self.full_address:
    #         try:
    #             geocoder = GoogleV3(api_key= GOOGLE_API_KEY)
    #             location = geocoder.geocode(self.full_address)
    #             self.latitude = location.latitude
    #             self.longitude = location.longitude
    #             print location
    #         except:
    #             print 'google api not working'
    #
    #
    # def save(self, *args, **kwargs):
    #     self.location()
    #     super(HealthCareCompany, self).save(*args, **kwargs)