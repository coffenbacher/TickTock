from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import *
from models import *

def show(request, name):
    i = Instrument.objects.get(pk=name)
    edit = True if i.seller.user == request.user else False
    if request.method == 'POST':
        form = InstrumentImageForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.instrument = i
            f.save()
    else:
        form = InstrumentImageForm()
    return render_to_response('inventory/show.html', RequestContext(request, {'i': i, 'edit': edit, 'form': form}))

def index(request):
    return render_to_response('inventory/create.html')

def create(request):
    return render_to_response('inventory/create.html')
