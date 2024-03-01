from rest_framework.serializers import ModelSerializer
from .models import (
    ProductModel, 
    ProductCategoryModel,
    BlogModel,
    BlogCategoryModel,
    FormModel,
    FormProductsModel
)


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


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategoryModel
        fields = "__all__"
        

class BlogCategorySerializer(ModelSerializer):
    class Meta:
        model = BlogCategoryModel
        fields = "__all__"


class BlogSerializer(ModelSerializer):
    class Meta:
        model = BlogModel
        fields = "__all__"


class FormSerializer(ModelSerializer):
    class Meta:
        model = FormModel
        fields = "__all__"


class FormProductSerializer(ModelSerializer):
    class Meta:
        model = FormProductsModel
        fields = "__all__"