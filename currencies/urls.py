#-*- coding:utf-8 -*-
from django.conf.urls.defaults import patterns, url
from .views import change_currency


urlpatterns = patterns('',
    url(r'^change/', change_currency, name='change_currency'),
)
