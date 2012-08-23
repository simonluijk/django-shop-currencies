from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from test_app.models import Product

urlpatterns = patterns('',
    # Examples:
    url(r'^$', ListView.as_view(model=Product), name='home'),
    url(r'^product/(?P<slug>[0-9A-Za-z-_.]+)/$', DetailView.as_view(model=Product),
        name='product_detail'),
    url(r'^currencies/', include('currencies.urls')),
    url(r'^cart/$', 'None', name="cart"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
