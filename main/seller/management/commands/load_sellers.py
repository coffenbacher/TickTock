import datetime, gzip, os, sys, zipfile
from django.contrib.auth.models import User
from BeautifulSoup import BeautifulSoup
from optparse import make_option

from django.core.management.base import NoArgsCommand

from seller.models import Seller, SellerCategory
from seller import models
import pdb

SELLER_DATA = os.path.abspath(os.path.join(os.path.dirname(models.__file__), 'data'))

class Command(NoArgsCommand):
    def allCountries(self, **options):
        fs = ['us.xml', 'us2.xml', 'canada.xml', 'world.xml', 'uk_cityonly.xml']#, 'world.xml', 'world2.xml']
        txt = ""
        for f in fs:
            tmp = os.path.join(SELLER_DATA, f)
            txt += open(tmp).read()
        soup = BeautifulSoup(txt)

        for s in soup.findAll('entry'):
            if s.find('name'):
                self.save_entry(s)

    def save_entry(self, e):
        d = {}
        fields = ['name', 'business_name', 'phone', 'email', 'website', 'address']
        truncate = ['first_name', 'email', 'last_name']

        for f in fields:
            d[f] = e.find(f).getText().strip() if e.find(f) else ""
        
        if not d['email']:
            d['email'] = d['name'].replace(' ', '_')
        
        if not d['business_name']:
            d['business_name'] = d['name']
        
        try:
            d['first_name'] = d['name'].split()[0]
            d['last_name'] = ' '.join(d['name'].split()[1:])
        except:
            d['first_name'] = d['name']
            d['last_name'] = ""

        for t in truncate:
            d[t] = d[t][:29]

        if not User.objects.filter(email=d['email']) and not User.objects.filter(username=d['email']):
            if d['email']:
                u = User.objects.create_user(
                    username=d['email'], 
                    password=d['email'], 
                    email=d['email'], 
                    first_name=d['first_name'],
                    last_name=d['last_name']
                    )
            else:
                print "%s failing" % e
        else:
            u = User.objects.get(username=d['email'])

        try:
            if not Seller.objects.filter(user=u):
                s = Seller.objects.create(user=u, name=d['business_name'], category=SellerCategory.objects.get_or_create(name='Luthier')[0], raw_address=d['address'])
            else:
                s = Seller.objects.get(user=u)
            
            try:
                if not s.location:
                    s.geocode()
                    print "Geocode succeeded for %s" % s
            except:
                    print "Geocode failed for %s" % s
        except:
            print "%s failing" % e



    def handle_noargs(self, **options):
        self.allCountries()
