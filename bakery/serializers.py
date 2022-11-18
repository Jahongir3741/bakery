from rest_framework.serializers import ModelSerializer
from .models import Bakery, Bread, BreadItem
from category.serailizers import CategorySerializer


class BakerySerializer(ModelSerializer):
    class Meta:
        model = Bakery
        fields = ['id','creator', 'owner', 'name', 'location', 'phone', 'open_at', 'close_at']


class BreadSerializer(ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Bread
        fields = ['id', 'name','category', 'price', 'text', 'image']


class BreadItemSerializer(ModelSerializer):
    class Meta:
        model = BreadItem
        fields = ['id', 'creator', 'bread', 'count']