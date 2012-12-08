from django.core.management.base import BaseCommand
from django.contrib.gis.utils import LayerMapping
import os

from location.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        def load_worlds(verbose=True):
            world_mapping = {
                'fips' : 'FIPS',
                'iso2' : 'ISO2',
                'iso3' : 'ISO3',
                'un' : 'UN',
                'name' : 'NAME',
                'area' : 'AREA',
                'pop2005' : 'POP2005',
                'region' : 'REGION',
                'subregion' : 'SUBREGION',
                'lon' : 'LON',
                'lat' : 'LAT',
                'mpoly' : 'MULTIPOLYGON',
            }

            WorldBorder.objects.all().delete()

            world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/world/TM_WORLD_BORDERS-0.3.shp'))
            lm = LayerMapping(WorldBorder, world_shp, world_mapping,
                              transform=False, encoding='iso-8859-1')
            lm.save(strict=True, verbose=verbose)

        load_worlds()
