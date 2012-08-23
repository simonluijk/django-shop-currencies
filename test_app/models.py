from django.db import models

from shop.models_bases import BaseProduct

from currencies.model_mixins import CurrenciesProductMixin


class Product(CurrenciesProductMixin, BaseProduct):
    pass
