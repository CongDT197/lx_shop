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
    # product_info = ListProductInfoSerializer(many=True)
    product_info = SerializerMethodField()
    product_type = serializers.CharField(source='get_product_type_display')

    def get_product_info(self, product):
        print('s')
        queryset = ProductInfo.objects.filter(product_id=product, is_active=True)
        return ListProductInfoSerializer(queryset, many=True).data

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
    product_info = CreateProductInfoSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'is_active': {'read_only': True},
        }

    @transaction.atomic()
    def update(self, instance, validated_data):
        list_product_info = validated_data.pop('product_info')
        list_product_info_old = ProductInfo.objects.filter(product_id=instance, is_active=True)
        for old_product_info in list_product_info_old:
            if old_product_info not in list_product_info:
                old_product_info.is_active = False
                old_product_info.save()
        for product_info in list_product_info:
            ProductInfo.objects.update_or_create(product_id=instance,
                                                 color=product_info['color'],
                                                 size=product_info['size'],
                                                 defaults={
                                                     'quantity': product_info['quantity'],
                                                     'color': product_info['color'],
                                                     'size': product_info['size'],
                                                     'is_active': True
                                                 })

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class DetailProductSerializer(ModelSerializer):
    product_info = SerializerMethodField()
    product_type = serializers.CharField(source='get_product_type_display')

    def get_product_info(self, product):
        print('s')
        queryset = ProductInfo.objects.filter(product_id=product, is_active=True)
        return ListProductInfoSerializer(queryset, many=True).data

    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'is_active': {'read_only': True},
        }


class DeleteProductSerializer(Serializer):
    set_id = serializers.ListField(
        child=serializers.IntegerField(required=True)
    )

