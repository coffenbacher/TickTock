from django.db import models
from photologue.models import ImageModel
from django_extensions.db.models import TimeStampedModel
from seller.models import *

# Create your models here.
class InstrumentImage(ImageModel):
    instrument = models.ForeignKey('Instrument')

class Maker(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class InstrumentType(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class InstrumentModel(TimeStampedModel):
    name = models.CharField(max_length=200)
    maker = models.ForeignKey('Maker')
    year = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Instrument(TimeStampedModel):
    model = models.ForeignKey(InstrumentModel)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=7)
    seller = models.ForeignKey(Seller)

    def __unicode__(self):
        return self.model.name
