#-*- coding:utf-8 -*-
from shop.cart.cart_modifiers_base import BaseCartModifier


class CurrenciesModifier(BaseCartModifier):
    """
    Cart modifier to set cart.currenct from state.
    """

    def pre_process_cart(self, cart, state):
        cart.currency = state['currency']
