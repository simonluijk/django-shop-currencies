class CurrenciesProductMixin(object):
    """
    A mixin to add multi currency support to your product models.
    """

    def get_price_in_currency(self, currency=None):
        """
        Returns the price in the provided currency.

        There is a template filter to provide the current currency.
        You can use it like this:

        {% load currencies %}
        {% price product %}
        {% price product "USD" %}
        ...
        """
        # NOTE: I have not implemented this method yet as I am using a custom
        # implementation because my prices are not attached to the product.
        # An implemention like chrisglass has done here would make sence.
        # http://bit.ly/tNpESg
        # Ofcourse you would use the Currency model above.
        return super(CurrenciesProductMixin, self).get_price()


class CurrenciesCartItemMixin(object):
    """
    A mixin to add currency support to your cart item models.
    """

    def get_price(self):
        """
        Override CartItem get_price method to return price bassed on
        self.cart.currency which is set by "currencies.cart_modifiers.CurrenciesModifier"
        so make sure you have put it in SHOP_CART_MODIFIERS setting.
        """
        # NOTE: Should rase a ImproperlyConfigured if currency is not set
        return self.product.get_price_in_currency(self.cart.currency)
