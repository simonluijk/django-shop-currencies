#-*- coding:utf-8 -*-
from decimal import Decimal
from django.conf import settings


def get_currency(request):
    try:
        return request.session['CURRENCY']
    except KeyError:
        return settings.SHOP_DEFAULT_CURRENCY


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
