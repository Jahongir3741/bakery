from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework.decorators import action
from .enums import Status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import response, status
from .permissions import IsClient

class OrderViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsClient]
    def get_queryset(self):
        queryset = Order.objects.filter(client = self.request.user)
        return queryset
    
    def get_serializer_class(self):
        serializer = OrderSerializer
        return serializer
    
    def perform_create(self, serializer):
        serializer.validata['client'] = self.request.user
        serializer.save()
    
    @action(methods=['PATCH'], detail=True, permission_classes=[IsAuthenticated, IsClient])
    def confirmed(self, request, *args, **kargs):
        obj = self.get_object()
        if obj.status == Status.NEW.name:
            obj.confirmed()
        return response.Response(data={"msg":"Buyurtma yulda"}, status=status.HTTP_200_OK)
    
    @action(methods=['PATCH'], detail=True, permission_classes=[IsAuthenticated, IsClient])
    def cancelled(self, request, *args, **kargs):
        obj = self.get_object()
        if obj.status == Status.NEW.name:
            obj.cancel()
            return response.Response(data={"msg":"Buyurtmani qaytardingiz?"}, status=status.HTTP_200_OK)
        elif obj.status == Status.CONFIRMED.name:
            return response.Response(data={"msg":"kechirasiz buyurtma yulga chiqib buldi endi qaytaraolmiysiz?"}, status=status.HTTP_200_OK)
    
    @action(methods=['PATCH'], detail=True, permission_classes=[IsAuthenticated, IsClient])
    def success(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.status == Status.CONFIRMED.name:
            obj.success()
        return response.Response(data={"msg":"Buyurtma mafaqyatli yetkazildi"})


class OrderItemAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsClient, IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        breadItem_id = kwargs.get("breadItem_id")
        count = request.data.get('count')
        breadItem_count = OrderItem.objects.get(bread_item=breadItem_id)
        serializer = OrderItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        try:
            breadItem_count.bread_item.counts(count)
        except Exception as e:
            return response.Response({"msg":e})
        return response.Response(status=status.HTTP_200_OK)
