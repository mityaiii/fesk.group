from rest_framework.serializers import ModelSerializer
from .models import ProductModel, CategoryModel


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        excluded_fields = kwargs.pop('excluded_fields', None)
        super(ProductSerializer, self).__init__(*args, **kwargs)

        if excluded_fields:
            for field_name in excluded_fields:
                self.fields.pop(field_name)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"
        