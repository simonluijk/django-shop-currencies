# -*- coding: utf-8 -*-
from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Currency, Country


class CurrencyTest(TestCase):
    def test_currency_rate(self):
        curr = Currency.objects.create(code=u'EUR', rate=Decimal('1.2222'),
            spread=Decimal('2.5'))

        self.assertEqual(curr.get_rate(), Decimal('1.2528'))


class ChangeCurrencyTest(TestCase):
    def setUp(self):
        Currency.objects.create(code=u'USD')
        Currency.objects.create(code=u'EUR')

    def test_change_currency(self):
        url = reverse('change_currency')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['CURRENCY'], settings.SHOP_DEFAULT_CURRENCY)

        response = self.client.post(url, data={'currency': u'USD'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['CURRENCY'], u'USD')

        response = self.client.post(url, data={'currency': u'eur'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['CURRENCY'], u'EUR')

        response = self.client.post(url, data={'currency': u'XXX'})
        self.assertEqual(response.status_code, 403)

        response = self.client.post(url)
        self.assertEqual(response.status_code, 400)


class CountryMiddlewareTest(TestCase):
    def setUp(self):
        self.url = reverse('change_currency')

    def test_country_middleware_success(self):
        response = self.client.get(self.url, REMOTE_ADDR=u'81.20.213.203')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['COUNTRY_CODE'], u'FR')

    def test_country_middleware_fail1(self):
        response = self.client.get(self.url, REMOTE_ADDR=u'127.0.0.1')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['COUNTRY_CODE'], u'')

    def test_country_middleware_fail2(self):
        response = self.client.get(self.url, REMOTE_ADDR=u'Bad IP address')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['COUNTRY_CODE'], u'')


class CurrencyMiddlewareTest(TestCase):
    def setUp(self):
        self.url = reverse('change_currency')
        eur = Currency.objects.create(code=u'EUR')
        usd = Currency.objects.create(code=u'USD')
        Country.objects.create(code=u'US', currency=usd)
        Country.objects.create(code=u'FR', currency=eur)

    def test_currency_middleware_success1(self):
        response = self.client.get(self.url, REMOTE_ADDR=u'81.20.213.203')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['CURRENCY'], u'EUR')

    def test_currency_middleware_success2(self):
        response = self.client.get(self.url, REMOTE_ADDR=u'74.125.39.104')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['CURRENCY'], u'USD')

    def test_currency_middleware_fail(self):
        response = self.client.get(self.url, REMOTE_ADDR=u'Bad IP address')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['CURRENCY'], settings.SHOP_DEFAULT_CURRENCY)
