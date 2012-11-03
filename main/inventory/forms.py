from models import *
from django.forms import ModelForm
from django.forms import CharField

class InstrumentImageForm(ModelForm):
    class Meta:
        model = InstrumentImage
        exclude = ('instrument', 'effect', 'crop_from')

class InstrumentForm(ModelForm):
    _type = CharField(label="Instrument Type (i.e. Violin)")
    _maker = CharField(label="Maker")
    _model = CharField(label="Model")

    class Meta:
        model = Instrument
        fields = ('_type', '_maker', '_model', 'price', 'description')
        exclude = ('seller', 'maker', 'model')

