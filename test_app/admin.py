from django.contrib import admin

from test_app.models import Product
from currencies.models import Price


class PriceInline(admin.TabularInline):
    model = Price

class ProductAdmin(admin.ModelAdmin):
    inlines = [PriceInline,]


admin.site.register(Product, ProductAdmin)
