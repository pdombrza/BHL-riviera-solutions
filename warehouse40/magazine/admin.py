from django.contrib import admin
from .models import Product, WarehouseZone, Worker, Order, ProductOrder


admin.site.register(Product)
admin.site.register(WarehouseZone)
admin.site.register(Worker)
admin.site.register(Order)
admin.site.register(ProductOrder)
