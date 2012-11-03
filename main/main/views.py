from inventory.models import *
import json
from seller.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def map(request):
    ins = Instrument.objects.all()
    ins_types = InstrumentType.objects.all()
    makers = Maker.objects.all()
    ins_models = InstrumentModel.objects.all()
    return render_to_response('map.html', {'ins': ins, 'ins_types': ins_types, 'makers': makers, 'ins_models': ins_models}, context_instance=RequestContext(request))

def map_search(request):
    i = s()
    #sellers = Seller.objects.filter(id__in=[x.seller_id for x in i])
    sellers = Seller.objects.all()
    return HttpResponse(json.dumps(list(sellers.values('id', 'lat', 'lng'))))

def home(request):
    return render_to_response('home.html')

def s():
    i = Instrument.objects.all()
    return i
    
