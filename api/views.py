from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

from django.shortcuts import get_object_or_404

from .models import (
    ProductModel,
    ProductCategoryModel,
    BlogModel,
    BlogCategoryModel,
    ProductFormModel,
    FormProductsModel,
    ContactFormModel
)
from .serializers import (
    ProductSerializer, 
    ProductCategorySerializer,
    BlogSerializer,
    BlogCategorySerializer,
    FormSerializer,
    FormProductSerializer,
    ContactFormSerializer
)


class ProductView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        product_id = self.request.query_params.get('id')

        if product_id:
            return ProductModel.objects.filter(id=product_id).first()

        for param in self.request.query_params:
            if 'title' in param:
                return ProductModel.objects.filter(**{param: self.request.query_params.get(param)}).first()
        return ProductModel.objects.all()
    
    
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            product = get_object_or_404(ProductModel, id=kwargs['pk'])
            serializer = self.get_serializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK) 

        queryset = self.get_queryset()
        page_size = self.request.query_params.get('page_size')
        page_number = self.request.query_params.get('page_number')

        self.paginator.page_size = page_size if page_size else self.paginator.page_size
        self.request.page = page_number if page_number else 1 

        page = self.paginator.paginate_queryset(queryset, request)

        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data) 
    

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
        product_category_id = self.request.query_params.get('id')

        if product_category_id:
            return ProductCategoryModel.objects.filter(id=product_category_id).first()

        for param in self.request.query_params:
            if 'title' in param:
                return ProductCategoryModel.objects.filter(**{param: self.request.query_params.get(param)}).first()
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
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]

    search_fields = ['title_ru', 'title_kz', 'title_en']

    def get_queryset(self):
        blog_id = self.request.query_params.get('id')

        if blog_id:
            return BlogModel.objects.filter(id=blog_id).first()
        
        return BlogModel.objects.all()
    
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            blog = get_object_or_404(BlogModel, id=kwargs['pk'])
            serializer = self.get_serializer(blog)
            return Response(serializer.data, status=status.HTTP_200_OK) 

        queryset = self.filter_queryset(self.get_queryset())

        page_size = self.request.query_params.get('page_size')
        page_number = self.request.query_params.get('page_number')

        self.paginator.page_size = page_size if page_size else self.paginator.page_size
        self.request.page = page_number if page_number else 1 

        page = self.paginator.paginate_queryset(queryset, request)

        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        blog_id = kwargs.get('pk')
        instance = BlogModel.objects.get(id=blog_id)

        excluded_fields  = None
        if not('image' in request.data):
            excluded_fields = ['image']

        serializer = BlogSerializer(instance, excluded_fields=excluded_fields, partial=True)

        serializer_data = serializer.data
        serializer_data.update(request.data)

        serializer = BlogSerializer(instance, data=serializer_data, excluded_fields=excluded_fields, partial=True)
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
        blog_category_id = self.request.query_params.get('id')

        if blog_category_id:
            return BlogCategoryModel.objects.filter(id=blog_category_id).first()

        for param in self.request.query_params:
            if 'title' in param:
                return BlogCategoryModel.objects.filter(**{param: self.request.query_params.get(param)}).first()
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
        form_id = self.request.query_params.get('id')

        if form_id:
            return ProductFormModel.objects.filter(id=form_id).first()

        return ProductFormModel.objects.all()
    
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            product = get_object_or_404(ProductFormModel, id=kwargs['pk'])
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
        instance = ProductFormModel.objects.get(id=category_id)

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
        form_id = self.request.query_params.get('id')

        if form_id:
            return FormProductsModel.objects.filter(id=form_id).first()

        return FormProductsModel.objects.all()
    
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            form = get_object_or_404(FormProductsModel, id=kwargs['pk'])
            serializer = self.get_serializer(form)
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
        instance = ContactFormModel.objects.get(id=category_id)

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
    

class ContactFormView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = ContactFormSerializer

    def get_queryset(self):
        form_id = self.request.query_params.get('id')

        if form_id:
            return ContactFormModel.objects.filter(id=form_id).first()

        return ContactFormModel.objects.all()
    
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            form = get_object_or_404(ContactFormModel, id=kwargs['pk'])
            serializer = self.get_serializer(form)
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
        instance = ContactFormModel.objects.get(id=category_id)

        serializer = ContactFormSerializer(instance)

        serializer_data = serializer.data
        serializer_data.update(request.data)

        serializer = ContactFormModel(instance, data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "form was deleted successfully"}, status=status.HTTP_204_NO_CONTENT)