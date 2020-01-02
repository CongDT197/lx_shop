from django.db import transaction
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from cart_management.cart_product_serializer import ListCartProductSerializer, \
    CreateEditCartProductSerializer
from cart_management.models import Cart, CartProduct
from commons.constrain import CONFIRMED
from commons.error_code import ValidationError
from product_management.models import Product


class ListCartSerializer(ModelSerializer):
    cart_product_id = ListCartProductSerializer(many=True)
    pay_type = serializers.CharField(source='get_pay_type_display')

    class Meta:
        model = Cart
        fields = '__all__'


class CreateCartSerializer(ModelSerializer):
    product_info = CreateEditCartProductSerializer(many=True, required=False)

    class Meta:
        model = Cart
        fields = '__all__'
        extra_kwargs = {
            'is_active': {'read_only': True},
            'price': {'read_only': True},
            'user_id': {'read_only': True},
        }

    @transaction.atomic()
    def create(self, validated_data):
        user = self.context.get('request').user
        try:
            cart_product = validated_data.pop('product_info')
        except KeyError:
            raise ValidationError('PRODUCT_INFO_REQUIRED')
        real_price = 0
        cart = Cart.objects.create(user_id=user, price=0, **validated_data)
        for item in cart_product:
            product_info = item['product_info_id']
            quantity = item['quantity']
            real_price += (product_info.product_id.price * quantity)
            if (item['product_info_id'].quantity - item['quantity']) < 0:
                raise ValidationError('ENOUGH_PRODUCT_QUANTITY')
            product_info.quantity -= quantity
            product_info.save()
            CartProduct.objects.create(cart_id=cart, **item)
        cart.price = real_price
        cart.save()
        return cart


class EditCartSerializer(ModelSerializer):
    product_info = CreateEditCartProductSerializer(many=True, required=False)

    def validate_product_info(self, value):
        for new_cart_product in value:
            product_info = new_cart_product['product_info_id']
            quantity = new_cart_product['quantity']
            if (product_info.quantity - quantity) < 0:
                raise ValidationError('ENOUGH_PRODUCT_QUANTITY')

        return value

    class Meta:
        model = Cart
        fields = '__all__'
        extra_kwargs = {
            'is_active': {'read_only': True},
            'price': {'read_only': True},
            'user_id': {'read_only': True},
        }

    @transaction.atomic()
    def update(self, instance, validated_data):
        if instance.status >= CONFIRMED:
            raise ValidationError('CART_CANNOT_CHANGE')
        list_new_cart_product = validated_data.pop('product_info')
        list_old_cart_product = list(CartProduct.objects.filter(cart_id=instance))
        real_price = 0

        for new_cart_product in list_new_cart_product:
            product_info = new_cart_product['product_info_id']
            quantity = new_cart_product['quantity']
            real_price += (product_info.product_id.price * quantity)

        for new_cart_product in list_new_cart_product:
            product_info = new_cart_product['product_info_id']
            quantity = new_cart_product['quantity']
            cart_product_temp = 0
            for old_cart_product in list_old_cart_product:
                if old_cart_product.product_info_id == product_info:
                    cart_product_temp = old_cart_product
                    list_old_cart_product.remove(old_cart_product)
            if cart_product_temp != 0:
                product_info.quantity = product_info.quantity - (quantity - cart_product_temp.quantity)
                product_info.save()
            else:
                product_info.quantity = product_info.quantity - quantity
                product_info.save()
            CartProduct.objects.update_or_create(cart_id=instance,
                                                 product_info_id=product_info,
                                                 defaults={
                                                     'quantity': quantity,
                                                     'is_active': True,
                                                 })
        for old_cart_product in list_old_cart_product:
            old_cart_product.is_active = False
            product_info = old_cart_product.product_info_id
            product_info.quantity += old_cart_product.quantity
            product_info.save()
            old_cart_product.quantity = 0
            old_cart_product.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.price=real_price
        instance.save()
        return instance


class DetailCartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        extra_kwargs = {
            'Cart_department': {'write_only': True},
            'is_active': {'read_only': True},
            'first_name': {'write_only': True},
            'date_joined': {'read_only': True},
            'password': {'write_only': True},
            'last_name': {'write_only': True},
            'last_login': {'write_only': True},
            'is_superCart': {'write_only': True},
            'is_staff': {'write_only': True},
            'groups': {'write_only': True},
            'Cart_permissions': {'write_only': True},
        }


class DeleteCartSerializer(Serializer):
    set_id = serializers.ListField(
        child=serializers.IntegerField(required=True)
    )
