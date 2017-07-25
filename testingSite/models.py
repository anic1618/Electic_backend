import string
from _ast import Str

from django.db import models

# -*- coding: utf-8 -*-

import pickle
import base64

from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from oauth2client import client, crypt

# from google.oauth2.
# from oauth2client.contrib.django_orm import FlowField
# from oauth2client.client import CredentialsField
'''
get out of shell and again go in when model is changed
'''

from decimal import Decimal


class Details(models.Model):
    def __unicode__(self):
        return self.user.username

    user = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)
    house_no = models.CharField(max_length=45)
    meter_id = models.CharField(max_length=100)


class Readings(models.Model):
    meter_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=datetime.now)
    readings = models.DecimalField(max_digits=20, decimal_places=10, default=Decimal('0.0000'))

    def __unicode__(self):
        return self.meter_id

    def __str__(self):
        return "%s  %s " % (self.timestamp.strftime('%m/%d/%Y'), self.readings)


class Readings_Daily(models.Model):
    meter_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=datetime.now)
    readings = models.DecimalField(max_digits=20, decimal_places=10, default=Decimal('0.0000'))

    def __str__(self):
        return self.house_no + '  ' + self.name


'''
class Userinfo(models.Model):
    email_id = models.CharField(primary_key=True, max_length=100)
    user_name = models.CharField(max_length=45, blank=True, null=True)
    picture_url = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.email_id + '  ' + self.user_name
'''
'''self.id = user.id
        self.email = user.email
        self.username = user.username
        self.first_name = user.first_name
        self.last_name = user.last_name'''


#
class PostData(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=250)
    url = models.CharField(max_length=1050)
    data = models.CharField(max_length=10050)
    meter_id = models.CharField(max_length=100)

    def __init__(self, user, data):
        self.id = user.id
        self.email = user.email
        self.username = user.username
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.data = data
        self.url = ''
        self.meter_id = ''

    def __str__(self):
        return self.email + self.data

    def set_url(self, url):
        self.url = url

    def set_meter_id(self, meter_id):
        self.meter_id = meter_id

    class Meta:  # dont create DB
        managed = False


'''
*_name field can be datetime ,will contains power consumed
'''


class Stats(models.Model):
    meter_id = models.CharField(primary_key=True, max_length=100)
    min_date = models.DateTimeField(blank=True, null=True)
    min_val = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    max_date = models.DateTimeField(blank=True, null=True)
    max_val = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    curr_val = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    avg_val = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)


    def __unicode__(self):
        return self.meter_id

    def __str__(self):
        return "Hourly Stats %s  %s  %s  %s  %s " % (
            self.meter_id, self.min_name, self.min_val, self.max_name, self.max_name)


class HourlyWiseStats(Stats):
    class Meta:
        managed = True


'''
class DayWiseStats(models.Model):
    meter_id = models.CharField(max_length=100)
    min_val = models.DecimalField(max_digits=20, decimal_places=10, default=Decimal('0.0000'))
    # min_name = models.CharField(max_length=10)
    min_name = models.DateTimeField()
    max_val = models.DecimalField(..., max_digits=19, decimal_places=10)
    # max_name = models.CharField(max_length=10)
    max_name = models.DateTimeField()
    curr_val = models.DecimalField(..., max_digits=19, decimal_places=10)
    avg_val = models.DecimalField(..., max_digits=19, decimal_places=10)

    def __unicode__(self):
        return self.meter_id

    def __str__(self):
        return "Hourly Stats %s  %s  %s  %s  %s " % (
            self.meter_id, self.min_name, self.min_val, self.max_name, self.max_name)


class WeekWiseStats(models.Model):
    meter_id = models.CharField(max_length=100)
    min_val = models.DecimalField(max_digits=20, decimal_places=10, default=Decimal('0.0000'))
    # min_name = models.CharField(max_length=10)
    min_name = models.DateTimeField()
    max_val = models.DecimalField(..., max_digits=19, decimal_places=10)
    # max_name = models.CharField(max_length=10)
    max_name = models.DateTimeField()
    curr_val = models.DecimalField(..., max_digits=19, decimal_places=10)
    avg_val = models.DecimalField(..., max_digits=19, decimal_places=10)

    def __unicode__(self):
        return self.meter_id

    def __str__(self):
        return "Hourly Stats %s  %s  %s  %s  %s " % (
            self.meter_id, self.min_name, self.min_val, self.max_name, self.max_name)


class MonthWiseStats(models.Model):
    meter_id = models.CharField(max_length=100)
    min_val = models.DecimalField(max_digits=20, decimal_places=10, default=Decimal('0.0000'))
    # min_name = models.CharField(max_length=10)
    min_name = models.DateTimeField()
    max_val = models.DecimalField(..., max_digits=19, decimal_places=10)
    # max_name = models.CharField(max_length=10)
    max_name = models.DateTimeField()
    curr_val = models.DecimalField(..., max_digits=19, decimal_places=10)
    avg_val = models.DecimalField(..., max_digits=19, decimal_places=10)

    def __unicode__(self):
        return self.meter_id

    def __str__(self):
        return "Hourly Stats %s  %s  %s  %s  %s " % (
            self.meter_id, self.min_name, self.min_val, self.max_name, self.max_name)


class YeariseStats(models.Model):
    meter_id = models.CharField(max_length=100)
    min_val = models.DecimalField(max_digits=20, decimal_places=10, default=Decimal('0.0000'))
    # min_name = models.CharField(max_length=10)
    min_name = models.DateTimeField()
    max_val = models.DecimalField(..., max_digits=19, decimal_places=10)
    # max_name = models.CharField(max_length=10)
    max_name = models.DateTimeField()
    curr_val = models.DecimalField(..., max_digits=19, decimal_places=10)
    avg_val = models.DecimalField(..., max_digits=19, decimal_places=10)

    def __unicode__(self):
        return self.meter_id

    def __str__(self):
        return "Hourly Stats %s  %s  %s  %s  %s " % (
            self.meter_id, self.min_name, self.min_val, self.max_name, self.max_name)
'''

'''
class SummaryStats(models.Model):
    hourly_Stats = HourlyWiseStats
    daily_Stats = DayWiseStats
    monthly_Stats = MonthWiseStats
    yearly_Stats = YearWiseStats

    class Meta:  # dont create DB
        managed = False

'''


class MyBackend(object):
    @staticmethod
    def authenticate(tokenId):
        try:
            # text = json.load(CLIENT_SECRETS)
            client_id = "1020251800466-qvcbo5u234p51dgmrik9dc0fvk2fmmjd.apps.googleusercontent.com"
            idinfo = client.verify_id_token(tokenId, client_id)
            # tokenId = request.POST['tokenId']
            # context = {'tokenId': tokenId}
            # return render(request, 'music/index.html', context)
            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise crypt.AppIdentityError("Wrong issuer.")
            user = User.objects.get(email=idinfo['email'])
            # user = None
            return user
        except crypt.AppIdentityError:
            return None
