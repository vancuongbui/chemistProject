from django.contrib import admin
from .models import Product, PriceRecord

# Register your models here.
admin.site.register(Product)
admin.site.register(PriceRecord)