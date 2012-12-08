# Create your views here.
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.db.models import Avg
from models import *
from forms import *
from inventory.forms import *
from inventory.models import *
from django.http import HttpResponse
import json
from django.shortcuts import render_to_response, redirect

def create(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        userform = UserForm(request.POST)
        if form.is_valid() and userform.is_valid():
            u = User.objects.create_user(request.POST['email'], request.POST['email'], request.POST['password'])
            f = form.save(commit=False)
            f.user = u
            f.save()
            f.geocode()

            u = authenticate(username=request.POST['email'], password=request.POST['password'])
            login(request, u)
            return redirect('/dealer/%s' % f.slugify())
    else:
        form = SellerForm()
        userform = UserForm()
    return render_to_response('seller/create.html', RequestContext(request, {'form': form, 'userform': userform}))


def show(request, name):
    s = Seller.objects.get(name=name.replace('_', ' '))
    edit = True if request.user == s.user else False

    if request.method == 'POST' and edit:
        form = InstrumentForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)

            i_type = InstrumentType.objects.get_or_create(name=request.POST['_type'])[0]
            i_maker = Maker.objects.get_or_create(name=request.POST['_maker'])[0]
            i_model = InstrumentModel.objects.get_or_create(name=request.POST['_model'], instrument_type=i_type, maker=i_maker)[0]

            f.model = i_model 
            f.seller = request.user.seller
            f.save()
    else:
        form = InstrumentForm()
    
    return render_to_response('seller/show.html', RequestContext(request, {'s': s, 'edit': edit, 'form': form}))

def index(request, **kwargs):
    if 'location__country' in kwargs:
        zoom = 4
        sellers = Seller.objects.filter(location__country=kwargs['location__country'])
    else:
        zoom = 2
        sellers = Seller.objects.all()

    center_lat = sellers.aggregate(Avg('location__lat'))['location__lat__avg']
    center_lng = sellers.aggregate(Avg('location__lng'))['location__lng__avg']

    if 'json' in request.GET:
        return HttpResponse(json.dumps(list(sellers.values('id', 'location__lat', 'location__lng'))))
    
    return render_to_response('seller/index.html', {'s': sellers,
                                                    'center_lat': center_lat,
                                                    'center_lng': center_lng,
                                                    'zoom': zoom})

