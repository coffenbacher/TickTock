from django_extensions.db.models import TimeStampedModel
from django.contrib.gis.db import models
from django.contrib.auth.models import User
# Create your models here.
class SellerCategory(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Seller(TimeStampedModel):
    name = models.CharField(max_length=200, verbose_name='Name (your name or your business)')
    user = models.OneToOneField(User, unique=True)
    subtitle = models.CharField(max_length=500)
    category = models.ForeignKey(SellerCategory,default=1)
    address = models.TextField(verbose_name="Address / Location")
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    def slugify(self):
        return self.name.replace(' ','_')

    def geocode(self):
        #try:
        import urllib, urllib2
        import json
        a = urllib.quote(self.address.replace(' ', '+').replace('\n', '+').strip())
        url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % a
        request = urllib2.urlopen(url)
        j = json.loads(request.read())
        self.lat = float(j['results'][0]['geometry']['location']['lat'])
        self.lng = float(j['results'][0]['geometry']['location']['lng'])
        self.save()


    def __unicode__(self):
        return self.name
