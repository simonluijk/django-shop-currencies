# -*- coding:utf-8 -*-
from django import template
from shop.models_bases import BaseCart, BaseCartItem, BaseOrder, BaseOrderItem
from shop.models import ExtraOrderPriceField
from ..models import Currency
from ..utils import currency_fmt, get_currency


register = template.Library()


def get_price(context, obj, attr, currency=None):
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
    elif currency is None:
        currency = get_currency(context['request'])

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


@register.simple_tag(takes_context=True)
def price(context, obj, attr=None, currency=None):
    """
    Template tag that takes a object and returns its price formatted in a
    currency. If currency is not passed it is taken from the request.
    """

    try:
        price, currency = get_price(context, obj, attr, currency)
        return u' '.join([currency.before, price, currency.after]).strip()
    except (KeyError, AttributeError, Currency.DoesNotExist), e:
        return u''


@register.simple_tag(takes_context=True)
def price_nofmt(context, obj, attr=None, currency=None):
    """
    Same as above but does not append/prepend currency symbols
    """

    try:
        price, currency = get_price(context, obj, attr, currency)
        return price
    except (KeyError, AttributeError, Currency.DoesNotExist), e:
        return u''
