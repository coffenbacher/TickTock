from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'seller.views.index'),
    url(r'^country/(?P<location__country>.*)/$', 'seller.views.index'),
    url(r'^state/(?P<location__state>.*)/$', 'seller.views.index'),
    url(r'^create/$', 'seller.views.create'),
    url(r'^(?P<name>.*)/$', 'seller.views.show'),
)

