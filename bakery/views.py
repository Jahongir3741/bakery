from rest_framework.viewsets import ModelViewSet
from .models  import Bakery, Bread, BreadItem
from .serializers import BakerySerializer, BreadSerializer, BreadItemSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwner, IsNotClientPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter


class BakeryViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated ,IsOwner]

    def get_queryset(self):
        queryset = Bakery.objects.all()
        return queryset
    
    def get_serializer_class(self):
        serializer = BakerySerializer
        return serializer


class BreadViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsNotClientPermission]
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    ordiring_fields = ['price', '-price']
    search_fields = ['name', 'text', 'category__name']


    def get_queryset(self):
        queryset = Bread.objects.all()
        return queryset
    
    def get_serializer_class(self):
        serializer = BreadSerializer
        return serializer
    
    def perform_create(self, instance):
        instance.creator = self.request.user
        instance.save()


class BreadItemViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = BreadItem.objects.all()
        return queryset
    
    def get_serializer_class(self):
        serializer = BreadItemSerializer
        return serializer