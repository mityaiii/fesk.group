from rest_framework.serializers import ModelSerializer
from .models import ProductModel, CategoryModel


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"
        