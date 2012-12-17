# Create your views here.
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.db.models import Avg, Count
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
    elif request.method == 'POST':
        form = InstrumentForm()
        message = "Thanks for your message! We'll get back to you as soon as possible."
        contact = SellerContactForm(request.POST)
        if contact.is_valid():
            c = contact.save(commit=False)
            c.seller = s
            c.save()
    else:
        form = InstrumentForm()
        contact = SellerContactForm()
        message = False
    
    return render_to_response('seller/show.html', RequestContext(request, {'s': s, 'edit': edit, 'form': form, 'contact': contact, 'message': message}))

def index(request, **kwargs):
    options, option_level, selected = False, False, False
    if 'location__country' in kwargs:
        zoom = 4
        sellers = Seller.objects.filter(location__country=kwargs['location__country'])
        selected = kwargs['location__country']
        options = sellers.values_list('location__administrative_area_level_1').annotate(count=Count('location__administrative_area_level_1')).order_by('location__administrative_area_level_1')
        option_level = {'url': 'state', 'label': 'State / Province'}
    elif 'location__state' in kwargs:
        zoom = 6
        sellers = Seller.objects.filter(location__administrative_area_level_1=kwargs['location__state'])
        selected = kwargs['location__state']
    else:
        zoom = 2
        sellers = Seller.objects.all()
        options = SellerLocation.objects.values_list('country').annotate(count=Count('country')).order_by('country')
        option_level = {'url': 'country', 'label': 'Country'}

    center_lat = sellers.aggregate(Avg('location__lat'))['location__lat__avg']
    center_lng = sellers.aggregate(Avg('location__lng'))['location__lng__avg']

    if 'json' in request.GET:
        return HttpResponse(json.dumps(list(sellers.values('id', 'name', 'location__lat', 'location__lng', 'sellerconfirmation__confirm'))))
    
    return render_to_response('seller/index.html', {'s': sellers,
                                                    'center_lat': center_lat,
                                                    'center_lng': center_lng,
                                                    'zoom': zoom,
                                                    'options': options,
                                                    'option_level': option_level,
                                                    'selected': selected})

