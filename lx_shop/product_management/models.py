from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import CASCADE, Model
from djmoney.models.fields import MoneyField

from commons.constrain import DIGITAL, MEN_WEAR, WOMEN_WEAR, HEAL, \
    FASHION, BABY, GENERAL, S, M, L, XL, NONE_COLOR, NONE_SIZE, BLUE, BLACK, YELLOW, RED

PRODUCT_TYPE = (
    (DIGITAL, 'DIGITAL'),
    (MEN_WEAR, 'MEN_WEAR'),
    (WOMEN_WEAR, 'WOMEN_WEAR'),
    (HEAL, 'HEAL'),
    (BABY, 'BABY'),
    (FASHION, 'FASHION'),
    (GENERAL, 'GENERAL'),
)
SIZE = (
    (S, 'S'),
    (M, 'M'),
    (L, 'L'),
    (XL, 'XL'),
    (NONE_SIZE, 'NONE_SIZE'),
)
COLOR = (
    (RED, 'RED'),
    (YELLOW, 'YELLOW'),
    (BLACK, 'BLACK'),
    (BLUE, 'BLUE'),
    (NONE_COLOR, 'NONE_COLOR'),
)


class Product(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False, validators=[MinLengthValidator(5)])
    description = models.CharField(max_length=120, null=False, blank=False, validators=[MinLengthValidator(5)])
    price = MoneyField(decimal_places=2, default_currency='USD', max_digits=11)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProductInfo(models.Model):
    product_id = models.ForeignKey(Product, null=False, on_delete=CASCADE)
    quantity = models.SmallIntegerField(null=False, blank=False)
    product_type = models.SmallIntegerField(choices=PRODUCT_TYPE, null=False, default=GENERAL)
    color = models.SmallIntegerField(choices=COLOR, null=False, default=NONE_COLOR)
    size = models.SmallIntegerField(choices=SIZE, null=False, default=NONE_SIZE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product_id.name
