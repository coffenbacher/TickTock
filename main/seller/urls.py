from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'seller.views.index'),
    url(r'^(?P<name>\w+)$', 'seller.views.show'),
)

