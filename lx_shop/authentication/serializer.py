from django.contrib.auth import authenticate
from django.core.validators import MinLengthValidator
from rest_framework import serializers
from rest_framework.serializers import Serializer

from commons.error_code import ValidationError
from user_management.models import User


class LoginSerializer(Serializer):
    email = serializers.EmailField(max_length=64, validators=[MinLengthValidator(8)])
    password = serializers.CharField(max_length=128, validators=[MinLengthValidator(2)])

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise ValidationError('LOGIN_FAILED')
        return data
