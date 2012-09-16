from inventory.models import *
import json
from seller.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response

def map(request):
    return render_to_response('map.html')

def map_search(request):
    i = s()
    #sellers = Seller.objects.filter(id__in=[x.seller_id for x in i])
    sellers = Seller.objects.all()
    return HttpResponse(json.dumps(list(sellers.values('id', 'lat', 'lng'))))

def s():
    i = Instrument.objects.all()
    return i
    
