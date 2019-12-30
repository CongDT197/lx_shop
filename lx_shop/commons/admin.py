from django.contrib import admin

# Register your models here.
from bank_management.models import UserBank, Bank
from cart_management.models import Cart, CartProduct
from product_management.models import Product, ProductInfo
from user_management.models import User

admin.site.register(User)
admin.site.register(UserBank)
admin.site.register(Bank)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Product)
admin.site.register(ProductInfo)
