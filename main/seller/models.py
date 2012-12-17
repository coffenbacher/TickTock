from django_extensions.db.models import TimeStampedModel
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
import pdb
# Create your models here.
class SellerCategory(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Seller(TimeStampedModel, models.Model):
    name = models.CharField(max_length=200, verbose_name='Name (your name or your business)')
    user = models.OneToOneField(User, unique=True)
    subtitle = models.CharField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(SellerCategory,default=1)
    location = models.ForeignKey('SellerLocation', null=True)
    raw_address = models.CharField(max_length=500, null=True, blank=True)

    objects = models.GeoManager()

    def slugify(self):
        return self.name.replace(' ','_')

    def geocode(self):
        import urllib, urllib2
        import json
        a = urllib.quote(self.raw_address.replace(' ', '+').replace('\n', '+').strip())
        url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % a
        request = urllib2.urlopen(url)
        j = json.loads(request.read())
        self.location = SellerLocation.create_from_json(j)
        self.save()


    def __unicode__(self):
        return self.name

class SellerLocation(TimeStampedModel):
    raw_json = models.TextField()
    json = models.TextField()
    formatted_address = models.CharField(max_length=500)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    pnt = models.PointField(null=True, blank=True)
    administrative_area_level_1 = models.CharField(max_length=100, null=True)
    administrative_area_level_2 = models.CharField(max_length=100, null=True)
    administrative_area_level_3 = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    postal_code = models.CharField(max_length=100, null=True)


    @classmethod
    def create_from_json(cls, j):
        d = {}
        d['raw_json'] = j
        d['json'] = j['results'][0]
        j = d['json']
        d['lat'] = j['geometry']['location']['lat']
        d['lng'] = j['geometry']['location']['lng']
        d['pnt'] = Point((d['lng'], d['lat']))         
        d['formatted_address'] = j['formatted_address']
        for c in j['address_components']:
            if 'administrative_area_level_1' in c['types']:
                d['administrative_area_level_1'] = c['long_name']
            if 'administrative_area_level_2' in c['types']:
                d['administrative_area_level_2'] = c['long_name']
            if 'administrative_area_level_3' in c['types']:
                d['administrative_area_level_3'] = c['long_name']
            if 'country' in c['types']:
                d['country'] = c['long_name']
            if 'postal_code' in c['types']:
                d['postal_code'] = c['long_name']
        return cls.objects.create(**d)        

class SellerConfirmation(TimeStampedModel):
    seller = models.ForeignKey(Seller)
    confirm = models.BooleanField()
    message = models.TextField()

class SellerContact(TimeStampedModel):
    seller = models.ForeignKey(Seller)
    email = models.CharField(max_length=200, verbose_name='Your email, so we can respond')
    message = models.TextField()

    def __unicode__(self):
        return "From: %s, To: %s" % (self.email, self.seller)

