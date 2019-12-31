from django.db import transaction
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.viewsets import GenericViewSet

from commons.error_code import ValidationError
from user_management.models import User
from user_management.serializer import ListUserSerializer, DetailUserSerializer, CreateUserSerializer, \
    EditUserSerializer, DeleteUserSerializer


@method_decorator(name='partial_update', decorator=swagger_auto_schema(auto_schema=None))
class UserAPIView(GenericViewSet,
                  ListModelMixin,
                  CreateModelMixin,
                  UpdateModelMixin,
                  RetrieveModelMixin):
    queryset = User.objects.filter(is_active=True)
    serializer_class = ListUserSerializer
    # authentication_classes = [ExpiringTokenAuthentication]
    # permission_classes = [IsLoggedInAdmin]
    lookup_field = 'id'

    serializer_method_classes = {
        'GET': DetailUserSerializer,
        'POST': CreateUserSerializer,
        'PUT': EditUserSerializer
    }

    def list(self, request, *args, **kwargs):
        queryset = User.objects.filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'status': True,
            'message': 'list user',
            'data': serializer.data},
            status=HTTP_201_CREATED
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            'status': True,
            'message': 'User created',
            'data': serializer.data},
            status=HTTP_201_CREATED
        )

    def update(self, request, *args, **kwargs):
        id = self.kwargs[self.lookup_field]
        queryset = User.objects.filter(id=id).filter(is_active=True)
        if queryset.count() == 0:
            raise ValidationError('USER_IS_DELETED_BY_ANOTHER_ADMIN')
        instance = self.get_object()
        if not instance.is_active == True:
            raise ValidationError('USER_IS_DELETED_BY_ANOTHER_ADMIN')

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'status': True,
            'message': 'User edited',
            'data': serializer.data
        }, status=HTTP_200_OK)

    @swagger_auto_schema(request_body=DeleteUserSerializer)
    @action(methods=['DELETE'], detail=False)
    @transaction.atomic()
    def delete(self, request):
        set_id = request.data['set_id']
        # validate_set_id(set_id)
        queryset = User.objects.filter(id__in=set_id).filter(is_active=True)
        if queryset.count() == 0:
            raise ValidationError('USER_IS_DELETED_BY_ANOTHER_ADMIN')
        if queryset.update(is_active=False) > 0:
            return Response({'status': True,
                             'message': 'User deleted!',
                             }, status=HTTP_200_OK)
        else:
            raise ValidationError('DELETE_FAILED')

    def retrieve(self, request, *args, **kwargs):
        id = self.kwargs[self.lookup_field]
        queryset = User.objects.filter(pk=id).filter(is_active=True)
        if queryset.__len__() != 0:
            instance = queryset[0]
            serializer = self.get_serializer(instance)
            return Response({'status': True,
                             'message': "return success",
                             'data': serializer.data},
                            status=HTTP_200_OK)
        raise ValidationError('USER_IS_DELETED_BY_ANOTHER_ADMIN')

    def get_serializer_class(self):
        try:
            if self.action == "list":
                return ListUserSerializer
            return self.serializer_method_classes[self.request.method]
        except(KeyError, AttributeError):
            return super(UserAPIView, self).get_serializer_class()
