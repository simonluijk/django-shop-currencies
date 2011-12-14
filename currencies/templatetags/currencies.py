# -*- coding:utf-8 -*-
from django import template
from ..models import Currency
from ..utils import currency_fmt, get_currency


register = template.Library()


@register.simple_tag(takes_context=True)
def price(context, obj, currency=None):
    """
    Template tag that takes a object and returns its price formatted in a
    currency. If currency is not passed it is taken from the request.
    """

    if currency is None:
        try:
            currency = get_currency(context['request'])
        except KeyError:
            return u''

    try:
        currency = Currency.objects.get(code=currency)
    except Currency.DoesNotExist:
        return u''

    price = obj.get_price(currency)
    price = currency_fmt(price, currency.decimal_places, currency.separator,
        currency.decimal_point)

    return u'%s %s %s' % (
        currency.before, price, currency.after)
