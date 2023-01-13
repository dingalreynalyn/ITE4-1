from django.contrib import admin
from .models import ProductInfo, ShopProducts, Cart

# Register your models here.
admin.site.register(ProductInfo)
admin.site.register(ShopProducts)
admin.site.register(Cart)