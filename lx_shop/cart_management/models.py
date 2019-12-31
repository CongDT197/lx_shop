from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import CASCADE
from djmoney.models.fields import MoneyField
from commons.constrain import CONFIRMING, CONFIRMED, SHIPPING, RECEIVED, PAYBYCARD, PAYOFFLINE
from product_management.models import Product, ProductInfo
from user_management.models import User

STATUS = (
    (CONFIRMING, 'CONFIRMING'),
    (CONFIRMED, 'CONFIRMED'),
    (SHIPPING, 'SHIPPING'),
    (RECEIVED, 'RECEIVED'),

)

PAY_TYPE = (
    (PAYBYCARD, 'PAY_BY_CARD'),
    (PAYOFFLINE, 'PAY_OFFLINE'),
)


class CartProduct(models.Model):
    product_info_id = models.ForeignKey(ProductInfo, related_name='cart_product_product_info', on_delete=CASCADE)
    quantity = models.SmallIntegerField(null=False, blank=False)
    is_active = models.BooleanField(default=True)

class Cart(models.Model):
    user_id = models.ForeignKey(User, related_name='cart_user', on_delete=CASCADE)
    cart_product_id = models.ManyToManyField(CartProduct, related_name='cart_cart_product')
    address_receive = models.CharField(max_length=100, null=False, validators=[MinLengthValidator(10)])
    pay_type = models.SmallIntegerField(choices=PAY_TYPE, null=False, default=PAYOFFLINE)
    price = MoneyField(decimal_places=2, default_currency='USD', max_digits=11)
    status = models.SmallIntegerField(choices=STATUS, null=False, default=CONFIRMING)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)
    is_active = models.BooleanField(default=True)
