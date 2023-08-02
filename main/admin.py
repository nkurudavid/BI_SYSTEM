from django.contrib import admin
from main.models import *

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(StockMovement)

