from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'inventory.views.index'),
    url(r'^create/$', 'inventory.views.create'),
    url(r'^(?P<name>\w+)$', 'inventory.views.show'),
)

