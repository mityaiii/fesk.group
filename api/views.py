from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import (
    ProductModel,
    ProductCategoryModel,
    BlogModel,
    BlogCategoryModel,
    FormModel,
    FormProductsModel
)
from .serializers import (
    ProductSerializer, 
    ProductCategorySerializer,
    BlogSerializer,
    BlogCategorySerializer,
    FormSerializer,
    FormProductSerializer
)


class ProductView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product_id = self.request.query_params.get('product_id')

        if product_id:
            return ProductModel.objects.filter('product__id')

        language = self.request.query_params.get('language', 'ru')
        title_param = f'title_{language}'

        title_query = self.request.query_params.get(title_param)

        if title_query:
            return ProductModel.objects.filter(Q(**{f'{title_param}__icontains': title_query}))

        return ProductModel.objects.all()
    
    
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            product = get_object_or_404(ProductModel, id=kwargs['pk'])
            serializer = self.get_serializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK) 

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        instance = ProductModel.objects.get(id=product_id)

        excluded_fields  = None
        if not('image' in request.data):
            excluded_fields = ['image']

        serializer = ProductSerializer(instance, excluded_fields=excluded_fields, partial=True)

        serializer_data = serializer.data
        serializer_data.update(request.data)

        serializer = ProductSerializer(instance, data=serializer_data, excluded_fields=excluded_fields, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "product was deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class CategoryView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = ProductCategorySerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')

        if category_id:
            return ProductCategoryModel.objects.filter(id=category_id)

        language = self.request.query_params.get('language', 'ru')
        title_param = f'title_{language}'

        title_query = self.request.query_params.get(title_param)

        if title_query:
            return ProductCategoryModel.objects.filter(Q(**{f'{title_param}__icontains': title_query}))

        return ProductCategoryModel.objects.all()
    
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            product = get_object_or_404(ProductCategoryModel, id=kwargs['pk'])
            serializer = self.get_serializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK) 

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        category_id = kwargs.get('pk')
        instance = ProductCategoryModel.objects.get(id=category_id)

        serializer = ProductCategorySerializer(instance)

        serializer_data = serializer.data
        serializer_data.update(request.data)

        serializer = ProductCategorySerializer(instance, data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "category was deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    

class BlogView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        blog_id = self.request.query_params.get('blog_id')

        if blog_id:
            return BlogModel.objects.filter(id=blog_id)

        language = self.request.query_params.get('language', 'ru')
        title_param = f'title_{language}'

        title_query = self.request.query_params.get(title_param)

        if title_query:
            return ProductModel.objects.filter(Q(**{f'{title_param}__icontains': title_query}))

        return ProductModel.objects.all()
    
    
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            product = get_object_or_404(BlogModel, id=kwargs['pk'])
            serializer = self.get_serializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK) 

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        blog_id = kwargs.get('pk')
        instance = BlogModel.objects.get(id=blog_id)

        serializer = BlogSerializer(instance)

        serializer_data = serializer.data
        serializer_data.update(request.data)

        serializer = BlogSerializer(instance, data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "blog was deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class BlogCategoryView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = BlogCategorySerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')

        if category_id:
            return BlogCategoryModel.objects.filter(id=category_id)

        language = self.request.query_params.get('language', 'ru')
        title_param = f'title_{language}'

        title_query = self.request.query_params.get(title_param)

        if title_query:
            return BlogCategoryModel.objects.filter(Q(**{f'{title_param}__icontains': title_query}))

        return BlogCategoryModel.objects.all()
    
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            product = get_object_or_404(BlogCategoryModel, id=kwargs['pk'])
            serializer = self.get_serializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK) 

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        category_id = kwargs.get('pk')
        instance = BlogCategoryModel.objects.get(id=category_id)

        serializer = BlogCategorySerializer(instance)

        serializer_data = serializer.data
        serializer_data.update(request.data)

        serializer = BlogCategorySerializer(instance, data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "blog category was deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class FormView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = FormSerializer

    def get_queryset(self):
        form_id = self.request.query_params.get('form_id')

        if form_id:
            return FormModel.objects.filter(id=form_id)

        return FormModel.objects.all()
    
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            product = get_object_or_404(FormModel, id=kwargs['pk'])
            serializer = self.get_serializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK) 

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        category_id = kwargs.get('pk')
        instance = FormModel.objects.get(id=category_id)

        serializer = FormSerializer(instance)

        serializer_data = serializer.data
        serializer_data.update(request.data)

        serializer = FormSerializer(instance, data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "form was deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    

class FormProductView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = FormProductSerializer

    def get_queryset(self):
        form_id = self.request.query_params.get('form_id')

        if form_id:
            return FormProductsModel.objects.filter(id=form_id)

        return FormProductsModel.objects.all()
    
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            product = get_object_or_404(FormProductsModel, id=kwargs['pk'])
            serializer = self.get_serializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK) 

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        category_id = kwargs.get('pk')
        instance = FormModel.objects.get(id=category_id)

        serializer = FormProductSerializer(instance)

        serializer_data = serializer.data
        serializer_data.update(request.data)

        serializer = FormProductSerializer(instance, data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "form was deleted successfully"}, status=status.HTTP_204_NO_CONTENT)