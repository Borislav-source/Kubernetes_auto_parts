from django.contrib import admin

from AutoParts.store.models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)
