from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'seller.views.index'),
    url(r'^create/$', 'seller.views.create'),
    url(r'^(?P<name>\w+)$', 'seller.views.show'),
)

