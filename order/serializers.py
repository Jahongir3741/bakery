from rest_framework.serializers import ModelSerializer
from .models import Order, OrderItem


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','client', 'location', 'phone', 'status']
        extra_kwargs = {'client':{'read_only':True}}



class OrderItemSerializer(ModelSerializer):
    order = OrderSerializer()
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'bread', 'count']
