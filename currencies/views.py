#-*- coding:utf-8 -*-
from urlparse import urlsplit
from django import http
from shop.util.cart import get_or_create_cart
from shop.views.cart import CartDetails
from .models import Currency
from .utils import get_currency


def change_currency(request):
    """
    Redirect to a given url while changing the currency
    The url and the currency code need to be specified in the
    request parameters.
    """

    next = request.REQUEST.get('next', None)
    if not next:
        next = urlsplit(request.META.get('HTTP_REFERER', ''))[2]
    if not next:
        next = '/'

    if request.method == 'POST':
        try:
            code = request.POST.get('currency').upper()
            request.session["CURRENCY"] = Currency.objects.get(code=code).code
        except (AttributeError):
            return http.HttpResponse(status=400)
        except (Currency.DoesNotExist):
            return http.HttpResponse(status=403)

    return http.HttpResponseRedirect(next)


class CurrenciesCartStateMixin(object):
    """
    Mixin providing currency support.
    """

    def get_initial_cart_state(self):
        """
        Inject currency into state from request.
        """
        return {'currency': get_currency(self.request)}
