from django.db import transaction
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.viewsets import GenericViewSet

from cart_management.cart_serializer import ListCartSerializer, DetailCartSerializer, CreateCartSerializer, \
    EditCartSerializer, DeleteCartSerializer
from cart_management.models import Cart
from commons.error_code import ValidationError


@method_decorator(name='partial_update', decorator=swagger_auto_schema(auto_schema=None))
class CartAPIView(GenericViewSet,
                     ListModelMixin,
                     CreateModelMixin,
                     UpdateModelMixin,
                     RetrieveModelMixin):
    queryset = Cart.objects.filter(is_active=True)
    serializer_class = ListCartSerializer
    # authentication_classes = [ExpiringTokenAuthentication]
    # permission_classes = [IsLoggedInAdmin]
    lookup_field = 'id'

    serializer_method_classes = {
        'GET': DetailCartSerializer,
        'POST': CreateCartSerializer,
        'PUT': EditCartSerializer
    }

    def list(self, request, *args, **kwargs):
        queryset = Cart.objects.filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'status': True,
            'message': 'list Cart',
            'data': serializer.data},
            status=HTTP_201_CREATED
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            'status': True,
            'message': 'Cart created',
            'data': serializer.data},
            status=HTTP_201_CREATED
        )

    def update(self, request, *args, **kwargs):
        id = self.kwargs[self.lookup_field]
        queryset = Cart.objects.filter(id=id).filter(is_active=True)
        if queryset.count() == 0:
            raise ValidationError('Cart_IS_DELETED_BY_ANOTHER_ADMIN')
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if not instance.is_active == True:
            raise ValidationError('Cart_IS_DELETED_BY_ANOTHER_ADMIN')

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'status': True,
            'message': 'Cart edited',
            'data': serializer.data
        }, status=HTTP_200_OK)

    @swagger_auto_schema(request_body=DeleteCartSerializer)
    @action(methods=['DELETE'], detail=False)
    @transaction.atomic()
    def delete(self, request):
        set_id = request.data['set_id']
        # validate_set_id(set_id)
        queryset = Cart.objects.filter(id__in=set_id).filter(is_active=True)
        if queryset.count() == 0:
            raise ValidationError('Cart_IS_DELETED_BY_ANOTHER_ADMIN')
        if queryset.update(is_active=False) > 0:
            return Response({'status': True,
                             'message': 'Cart deleted!',
                             }, status=HTTP_200_OK)
        else:
            raise ValidationError('DELETE_FAILED')

    def retrieve(self, request, *args, **kwargs):
        id = self.kwargs[self.lookup_field]
        queryset = Cart.objects.filter(pk=id).filter(is_active=True)
        if queryset.__len__() != 0:
            instance = queryset[0]
            serializer = self.get_serializer(instance)
            return Response({'status': True,
                             'message': "return success",
                             'data': serializer.data},
                            status=HTTP_200_OK)
        raise ValidationError('Cart_IS_DELETED_BY_ANOTHER_ADMIN')

    def get_serializer_class(self):
        try:
            if self.action == "list":
                return ListCartSerializer
            return self.serializer_method_classes[self.request.method]
        except(KeyError, AttributeError):
            return super(CartAPIView, self).get_serializer_class()
