#-*- coding:utf-8 -*-
from django.contrib import admin
from .models import Currency, Country


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'rate', 'spread', 'before', 'after', 'decimal_places',
        'decimal_point', 'separator')
    list_editable = ('rate',)

admin.site.register(Currency, CurrencyAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('code', 'currency')

admin.site.register(Country, CountryAdmin)
