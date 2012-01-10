# -*- coding:utf-8 -*-
from django import template
from shop.models_bases import BaseCart, BaseCartItem, BaseOrder, BaseOrderItem
from shop.models import ExtraOrderPriceField
from ..models import Currency
from ..utils import format_price, format_price_nosym, get_currency


register = template.Library()


@register.simple_tag(takes_context=True)
def price(context, obj, attr=None, currency=None):
    """
    Template tag that takes a object and returns its price formatted in a
    currency. If currency is not passed it is taken from the request.
    """
    if currency is None:
        try:
            currency = get_currency(context['request'])
        except KeyError:
            pass

    return format_price(obj, attr, currency)


@register.simple_tag(takes_context=True)
def price_nofmt(context, obj, attr=None, currency=None):
    """
    Same as above but does not append/prepend currency symbols
    """
    if currency is None:
        try:
            currency = get_currency(context['request'])
        except KeyError:
            pass

    return format_price_nosym(obj, attr, currency)
