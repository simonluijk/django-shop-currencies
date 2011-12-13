# -*- coding: utf-8 -*-
import os
import pygeoip

from django.conf import settings
from .models import Country


# NOTE: I am using pygeoip instead of the geodjango geoip interface
# simple because my os provided GeoIP.dat file is not compatible with
# geodjango's api. It would be nice if it fellback to geojango's api
# if pygeoip is not installed.
geoip = pygeoip.GeoIP(os.path.join(settings.GEOIP_PATH, "GeoIP.dat"))


class GeoIP2CountryMiddleware(object):
    """
    Set COUNTRY_CODE session variable from REMOTE_ADDR
    """

    def process_request(self, request):
        if 'COUNTRY_CODE' in request.session.keys():
            return

        try:
            country_code = geoip.country_code_by_addr(request.META['REMOTE_ADDR'])
        except pygeoip.GeoIPError:
            country_code = u''
        request.session['COUNTRY_CODE'] = country_code


class Country2CurrencyMiddleware(object):
    """
    Set CURRENCY session variable from COUNTRY_CODE
    """

    def process_request(self, request):
        if 'CURRENCY' in request.session.keys():
            return

        try:
            country = Country.objects.get(code=request.session['COUNTRY_CODE'])
            request.session['CURRENCY'] = country.currency.code
        except Country.DoesNotExist:
            request.session['CURRENCY'] = settings.SHOP_DEFAULT_CURRENCY
