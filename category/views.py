from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serailizers import CategorySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class CategoryViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset
    
    def get_serializer_class(self):
        serializer = CategorySerializer
        return serializer