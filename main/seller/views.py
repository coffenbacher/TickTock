# Create your views here.
from models import *
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('seller/index.html')


def show(request, name):
    s = Seller.objects.get(name=name.replace('_', ' '))
    return render_to_response('seller/show.html', {'s': s})
