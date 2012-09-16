from django_extensions.db.models import TimeStampedModel
from django.contrib.gis.db import models
# Create your models here.
class SellerCategory(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Seller(TimeStampedModel):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(SellerCategory)
    lat = models.FloatField()
    lng = models.FloatField()

    def __unicode__(self):
        return self.name
