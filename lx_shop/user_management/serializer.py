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
from user_management.models import User
from user_management.validation import validate_unique_email


class ListUserSerializer(ModelSerializer):
    gender=serializers.CharField(source='get_gender_display')
    user_type=serializers.CharField(source='get_user_type_display')

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'date_joined': {'write_only': True},
            'last_login': {'write_only': True},
            'password': {'write_only': True},
            'last_name': {'write_only': True},
            'first_name': {'write_only': True},
            'is_superuser': {'write_only': True},
            'is_staff': {'write_only': True},
            'groups': {'write_only': True},
            'user_permissions': {'write_only': True},
        }


class CreateUserSerializer(ModelSerializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        user_list = User.objects.filter(email=value)
        for user in user_list:
            if user.is_active == True:
                raise ValidationError('EMAIL_UNIQUE')
            elif user.is_active == False:
                user.delete()
        return value

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise ValidationError('PHONE_NUMBER_MUST_BE_STRING_NUMBER')
        return value


    def validate_birthday(self, value):
        if datetime.now().year - value.year < 18:
            raise ValidationError('NOT_ENOUGH_AGE')
        return value


    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'user_department': {'write_only': True},
            'is_active': {'read_only': True},
            'first_name': {'read_only': True},
            'date_joined': {'read_only': True},
            'password': {'read_only': True},
            'last_name': {'read_only': True},
            'last_login': {'read_only': True},
            'is_superuser': {'read_only': True},
            'is_staff': {'read_only': True},
            'groups': {'read_only': True},
            'user_permissions': {'read_only': True},

        }

    @transaction.atomic()
    def create(self, validated_data):
        password = make_password(validated_data['phone_number'])
        user = User.objects.create(password=password, **validated_data)
        return user


class EditUserSerializer(ModelSerializer):
    email = serializers.EmailField()

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise ValidationError('PHONE_NUMBER_MUST_BE_STRING_NUMBER')
        return value

    def validate_birthday(self, value):
        if datetime.now().year - value.year < 18:
            raise ValidationError('NOT_ENOUGH_AGE')
        return value

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'user_department': {'write_only': True},
            'is_active': {'read_only': True},
            'first_name': {'read_only': True},
            'date_joined': {'read_only': True},
            'password': {'read_only': True},
            'last_name': {'read_only': True},
            'last_login': {'read_only': True},
            'is_superuser': {'read_only': True},
            'is_staff': {'read_only': True},
            'groups': {'read_only': True},
            'user_permissions': {'read_only': True},
        }

    @transaction.atomic()
    def update(self, instance, validated_data):
        validate_unique_email(instance, validated_data['email'])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class DetailUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'user_department': {'write_only': True},
            'is_active': {'read_only': True},
            'first_name': {'write_only': True},
            'date_joined': {'read_only': True},
            'password': {'write_only': True},
            'last_name': {'write_only': True},
            'last_login': {'write_only': True},
            'is_superuser': {'write_only': True},
            'is_staff': {'write_only': True},
            'groups': {'write_only': True},
            'user_permissions': {'write_only': True},
        }


class DeleteUserSerializer(Serializer):
    set_id = serializers.ListField(
        child=serializers.IntegerField(required=True)
    )


class ImportUserSerializer(Serializer):
    import_file = serializers.FileField()

