#-*- coding:utf-8 -*-
from .models import Currency
from .utils import get_currency


def currencies(request):
    return {
        'currencies': Currency.objects.all(),
        'currency': get_currency(request),
    }
