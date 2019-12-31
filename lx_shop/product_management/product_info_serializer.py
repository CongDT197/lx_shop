from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from commons.error_code import ValidationError
from product_management.models import ProductInfo


class ListProductInfoSerializer(ModelSerializer):
    color = serializers.CharField(source='get_color_display')
    size = serializers.CharField(source='get_size_display')

    class Meta:
        model = ProductInfo
        fields = '__all__'


class CreateProductInfoSerializer(ModelSerializer):

    def validate_quantity(self, value):
        if value < 1:
            raise ValidationError('QUANTITY_MIN_VALUE')
        if value > 10000:
            raise ValidationError('QUANTITY_MAX_VALUE')
        return value

    class Meta:
        model = ProductInfo
        fields = [
            'quantity',
            'color',
            'size'
        ]
