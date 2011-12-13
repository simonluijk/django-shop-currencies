# -*- coding:utf-8 -*-
from decimal import Decimal
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.core.exceptions import ImproperlyConfigured
from polymorphic.polymorphic_model import PolymorphicModel


class Currency(models.Model):
    """
    A currency model.
    """

    code = models.CharField(_(u'Code'), unique=True, max_length=3)
    rate = models.DecimalField(_(u'Rate'), max_digits=12, decimal_places=4,
        default=Decimal('1'))
    spread = models.DecimalField(_(u'Spread'), max_digits=12, decimal_places=4,
        default=Decimal('2.5'))
    before = models.CharField(_(u'Before chars'), max_length=30, blank=True,
        null=True)
    after = models.CharField(_(u'After chars'), max_length=30, blank=True,
        null=True)
    decimal_places = models.IntegerField(_(u'Decimal places'), default=2)
    separator = models.CharField(_(u'Thousand seperator'), max_length=1,
        default=u',')
    decimal_point = models.CharField(_(u'Decimal point'), max_length=1,
        default=u'.')

    class Meta:
        verbose_name = _(u'Currency')
        verbose_name_plural = _(u'Currencies')

    def __unicode__(self):
        return self.code

    def save(self, *args, **kwargs):
        self.code = self.code.upper()
        super(Currency, self).save(*args, **kwargs)

    def get_rate(self):
        rate = self.rate * (1 + (self.spread / 100))
        return Decimal(rate).quantize(Decimal('0.0001'))


class Country(models.Model):
    """
    A country model to map country code to a currency.
    """

    code = models.CharField(_(u'Code'), unique=True, max_length=2)
    currency = models.ForeignKey(Currency)

    class Meta:
        verbose_name = _(u'Country')
        verbose_name_plural = _(u'Countries')

    def __unicode__(self):
        return self.code

    def save(self, *args, **kwargs):
        self.code = self.code.upper()
        super(Country, self).save(*args, **kwargs)
