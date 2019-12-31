from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from cart_management.models import CartProduct
from commons.error_code import ValidationError
from product_management.models import ProductInfo, Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartProductProductInfoSerializer(ModelSerializer):
    product_id = ProductSerializer()

    class Meta:
        model = ProductInfo
        fields = '__all__'


class ListCartProductSerializer(ModelSerializer):
    product_info_id = CartProductProductInfoSerializer()

    class Meta:
        model = CartProduct
        fields = '__all__'


class CreateCartProductSerializer(ModelSerializer):
    product_info_id = serializers.StringRelatedField

    def validate_quantity(self, value):
        if value < 1:
            raise ValidationError('QUANTITY_MIN_VALUE')
        if value > 10000:
            raise ValidationError('QUANTITY_MAX_VALUE')
        return value

    class Meta:
        model = CartProduct
        fields = [
            'product_info_id',
            'quantity',
        ]
