from django.db import transaction
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from cart_management.cart_product_serializer import ListCartProductSerializer, CreateCartProductSerializer
from cart_management.models import Cart, CartProduct
from commons.constrain import CONFIRMED
from commons.error_code import ValidationError


class ListCartSerializer(ModelSerializer):
    cart_product_id = ListCartProductSerializer(many=True)
    pay_type = serializers.CharField(source='get_pay_type_display')

    class Meta:
        model = Cart
        fields = '__all__'


class CreateCartSerializer(ModelSerializer):
    cart_product_id = CreateCartProductSerializer(many=True)

    def validate_price(self, value):
        if value < 1:
            raise ValidationError('PRICE_MIN_VALUE')
        return value

    class Meta:
        model = Cart
        fields = '__all__'
        extra_kwargs = {
            'is_active': {'read_only': True},
            'price': {'read_only': True},
        }

    @transaction.atomic()
    def create(self, validated_data):
        cart_product = (validated_data.pop('cart_product_id'))
        real_price = 0
        set_cart_product = []
        for item in cart_product:
            real_price += (item['product_info_id'].product_id.price * item['quantity'])
            if (item['product_info_id'].quantity - item['quantity']) < 0:
                raise ValidationError('ENOUGH_PRODUCT_QUANTITY')
            cart_product_item = CartProduct.objects.create(**item)
            set_cart_product.append(cart_product_item)
        cart = Cart.objects.create(price=real_price, **validated_data)
        cart.cart_product_id.set(set_cart_product)
        cart.save()
        return cart


class EditCartSerializer(ModelSerializer):
    cart_product_id = CreateCartProductSerializer(many=True)

    def validate_price(self, value):
        if value < 1:
            raise ValidationError('PRICE_MIN_VALUE')
        return value

    class Meta:
        model = Cart
        fields = '__all__'
        extra_kwargs = {
            'is_active': {'read_only': True},
            'price': {'read_only': True},
        }

    @transaction.atomic()
    def update(self, instance, validated_data):
        if instance.status == CONFIRMED:
            raise ValidationError('CART_CANNOT_CHANGE')
        list_new_cart_product = validated_data.pop('cart_product_id')
        list_old_cart_product = instance.cart_product_id
        print(instance.cart_product_id)
        for cart_product in list_old_cart_product:
            if cart_product not in list_new_cart_product:
                # cart_product.is_active = False
                # cart_product.save()
                instance.cart_product_id.remove(cart_product)
        for cart_product_new in list_new_cart_product:
            new_cart_product = CartProduct.objects.update_or_create(product_info_id=cart_product_new['product_info_id'],
                                                                    defaults={'quantity': cart_product_new['quantity']})
            if new_cart_product not in list_old_cart_product:
                instance.cart_product_id.add(new_cart_product)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
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


class ImportCartSerializer(Serializer):
    import_file = serializers.FileField()
