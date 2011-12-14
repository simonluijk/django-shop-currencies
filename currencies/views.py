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


class CurrenciesCartDetailsMixin(object):
    """
    Mixin providing currency support.
    """

    def get_state_data(self):
        """
        Inject currency into state from request.
        """
        return {'currency': get_currency(self.request)}

    # NOTE: If a hook to get_state_data gets created in django-SHOP we can remove
    # this method.
    def get_context_data(self, **kwargs):
        # There is no get_context_data on super(), we inherit from the mixin!
        ctx = {}
        state = self.get_state_data()
        cart_object = get_or_create_cart(self.request)
        cart_object.update(state)
        ctx.update({'cart': cart_object})
        ctx.update({'cart_items': cart_object.get_updated_cart_items()})
        return ctx


class CurrenciesCartDetails(CurrenciesCartDetailsMixin, CartDetails):
    pass
