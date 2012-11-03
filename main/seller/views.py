# Create your views here.
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from models import *
from forms import *
from inventory.forms import *
from inventory.models import *
from django.shortcuts import render_to_response, redirect

def index(request):
    s = Seller.objects.all()
    return render_to_response('seller/index.html', {'s': s})

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
