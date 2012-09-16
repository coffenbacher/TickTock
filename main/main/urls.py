from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'main.views.home', name='home'),
    url(r'^map/$', 'main.views.map', name='map'),
    url(r'^map/search/$', 'main.views.map_search', name='map_search'),
    url(r'^dealer/', include('seller.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^photologue/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': 'photologue',
            'show_indexes': True
        }),
   )
