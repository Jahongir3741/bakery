from rest_framework.serializers import ModelSerializer
from .models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent', 'creator']
        extra_kwargs = {
            'creator':{'write_only':True}
        }
