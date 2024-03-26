from rest_framework.serializers import ModelSerializer
from .models import (
    ProductModel, 
    ProductCategoryModel,
    BlogModel,
    BlogCategoryModel,
    ProductFormModel,
    FormProductsModel,
    ContactFormModel,
    ProductImageModel
)

class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImageModel
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
    #     fields = ['title_ru', 'title_kz', 'title_en', 'price_ru', 'price_kz', 'description_ru', 'description_kz', 'image', 'category']

    # def get_products(self, instance):
    #     return instance.formproductsmodel_set.all()
    
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['products'] = ProductImageSerializer(self.get_products(instance), many=True).data
    #     return data

    # def create(self, validated_data):
    #     if 'image' in validated_data:
    #         product_images = validated_data.pop('image')
        
    #         form = ProductModel.objects.create(**validated_data)
    #         for product_data in product_images:
    #             ProductImageModel.objects.create(form=form, **product_data)

    #         return form
        
    #     return ProductFormModel.objects.create(**validated_data)


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

    def __init__(self, *args, **kwargs):
        excluded_fields = kwargs.pop('excluded_fields', None)
        super(BlogSerializer, self).__init__(*args, **kwargs)

        if excluded_fields:
            for field_name in excluded_fields:
                self.fields.pop(field_name)


class FormProductSerializer(ModelSerializer):
    class Meta:
        model = FormProductsModel
        fields = ['product_id', 'quantity']
        

class FormSerializer(ModelSerializer):
    products = FormProductSerializer(many=True, required=False)

    class Meta:
        model = ProductFormModel
        fields = ['fio', 'telephon', 'email', 'message', 'products']

    def get_products(self, instance):
        return instance.formproductsmodel_set.all()
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['products'] = FormProductSerializer(self.get_products(instance), many=True).data
        return data

    def create(self, validated_data):
        if 'products' in validated_data:
            products_data = validated_data.pop('products')
        
            form = ProductFormModel.objects.create(**validated_data)
            for product_data in products_data:
                FormProductsModel.objects.create(form=form, **product_data)

            return form
        
        return ProductFormModel.objects.create(**validated_data)


class ContactFormSerializer(ModelSerializer):
    class Meta:
        model = ContactFormModel
        fields = '__all__'
