#-*- coding:utf-8 -*-
from decimal import Decimal
from django.conf import settings
from django import template
from shop.models_bases import BaseCart, BaseCartItem, BaseOrder, BaseOrderItem
from shop.models import ExtraOrderPriceField
from .models import Currency


def get_currency(request):
    """
    Get currency from request. If no currency return SHOP_DEFAULT_CURRENCY
    """

    try:
        return request.session['CURRENCY']
    except KeyError:
        return settings.SHOP_DEFAULT_CURRENCY


def get_price(obj, attr, currency=None):
    """
    Helper function to get price
    """

    if isinstance(obj, tuple([BaseOrder, BaseCart])):
        currency = obj.currency

    elif isinstance(obj, BaseCartItem):
        currency = obj.cart.currency

    elif isinstance(obj, BaseOrderItem):
        currency = obj.order.currency

    elif isinstance(obj, ExtraOrderPriceField):
        currency = obj.order.currency
        attr = 'value'

    if not attr:
        price = obj.get_price_in_currency(currency)
    else:
        price = getattr(obj, attr)
        if callable(price):
            price = price()

    currency = Currency.objects.get(code=currency)
    price = currency_fmt(price, currency.decimal_places, currency.separator,
        currency.decimal_point)
    return [price, currency]


def format_price(obj, attr=None, currency=None):
    """
    Function that takes a object and returns its price formatted in a
    currency.
    """
    try:
        price, currency = get_price(obj, attr, currency)
        return u' '.join([currency.before, price, currency.after]).strip()
    except (KeyError, AttributeError, Currency.DoesNotExist), e:
        return u''


def format_price_nosym(obj, attr=None, currency=None):
    """
    Same as above but does not append/prepend currency symbols
    """
    try:
        price, currency = get_price(obj, attr, currency)
        return price
    except (KeyError, AttributeError, Currency.DoesNotExist), e:
        return u''


def currency_fmt(value, places=2, sep=',', dp='.'):
    """
    Convert Decimal to a Currency formatted string.

    places:  required number of places after the decimal point
    sep:     optional grouping separator (comma, period, space, or blank)
    dp:      decimal point indicator (comma or period)
             only specify as blank when places is zero
    """

    q = Decimal(10) ** - places  # 2 places --> '0.01'
    sign, digits, exp = value.quantize(q).as_tuple()
    result = []
    digits = map(str, digits)
    build, next = result.append, digits.pop
    for i in range(places):
        build(next() if digits else '0')
    build(dp)
    if not digits:
        build('0')
    i = 0
    while digits:
        build(next())
        i += 1
        if i == 3 and digits:
            i = 0
            build(sep)
    return ''.join(reversed(result))
