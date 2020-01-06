from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from authentication.serializer import LoginSerializer
from user_management.models import User


class LoginAPIView(GenericAPIView):

    @swagger_auto_schema(request_body=LoginSerializer)
    @action(methods=['post'], detail=False)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        email = data.get('email')
        user = User.objects.get(email=email)
        token, created = Token.objects.get_or_create(user=user)

        data = {
            'token': token.key
        }
        return Response({
            'status': True,
            'message': 'you are logined',
            'data': data
        })
