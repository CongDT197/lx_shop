# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from datetime import date, datetime

from django.contrib.auth.hashers import make_password
from django.core.validators import MinLengthValidator
from django.db import transaction
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.schemas.coreapi import is_custom_action
from rest_framework.serializers import ModelSerializer, Serializer
from commons.error_code import ValidationError
from product_management.models import Product, ProductInfo
from product_management.product_info_serializer import CreateProductInfoSerializer, ListProductInfoSerializer


class ListProductSerializer(ModelSerializer):
    product_info = ListProductInfoSerializer(many=True)
    product_type = serializers.CharField(source='get_product_type_display')

    class Meta:
        model = Product
        fields = '__all__'


class CreateProductSerializer(ModelSerializer):
    product_info = CreateProductInfoSerializer(many=True)

    def validate_price(self, value):
        if value == 0:
            raise ValidationError('PRICE_MIN_VALUE')
        return value

    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'is_active': {'read_only': True},
        }

    @transaction.atomic()
    def create(self, validated_data):
        product_info = (validated_data.pop('product_info'))
        product = Product.objects.create(**validated_data)
        for item in product_info:
            ProductInfo.objects.create(product_id=product, **item)
        return product


class EditProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'is_active': {'read_only': True},
        }

    @transaction.atomic()
    def update(self, instance, validated_data):
        # validate_unique_email(instance, validated_data['email'])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class DetailProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'Product_department': {'write_only': True},
            'is_active': {'read_only': True},
            'first_name': {'write_only': True},
            'date_joined': {'read_only': True},
            'password': {'write_only': True},
            'last_name': {'write_only': True},
            'last_login': {'write_only': True},
            'is_superProduct': {'write_only': True},
            'is_staff': {'write_only': True},
            'groups': {'write_only': True},
            'Product_permissions': {'write_only': True},
        }


class DeleteProductSerializer(Serializer):
    set_id = serializers.ListField(
        child=serializers.IntegerField(required=True)
    )


class ImportProductSerializer(Serializer):
    import_file = serializers.FileField()
