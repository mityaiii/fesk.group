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


class FormProductSerializer(ModelSerializer):
    class Meta:
        model = FormProductsModel
        fields = ['product_id', 'quantity']
        

class FormSerializer(ModelSerializer):
    products = FormProductSerializer(many=True, required=False)

    class Meta:
        model = FormModel
        fields = ['fio', 'telephon', 'email', 'message', 'products']

    def get_products(self, instance):
        return instance.formproductsmodel_set.all()
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['products'] = FormProductSerializer(self.get_products(instance), many=True).data
        return data

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        form = FormModel.objects.create(**validated_data)
        for product_data in products_data:
            FormProductsModel.objects.create(form=form, **product_data)
        return form