from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin
from .models import Product, Order, Delivery

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Delivery)
