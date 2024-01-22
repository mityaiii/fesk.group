from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import ProductModel, CategoryModel
from .serializers import ProductSerializer, CategorySerializer


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

        serializer = ProductSerializer(instance)

        serializer_data = serializer.data
        serializer_data.update(request.data)

        serializer = ProductSerializer(instance, data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "product was deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class CategoryView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')

        if category_id:
            return CategoryModel.objects.filter(id=category_id)

        language = self.request.query_params.get('language', 'ru')
        title_param = f'title_{language}'

        title_query = self.request.query_params.get(title_param)

        if title_query:
            return CategoryModel.objects.filter(Q(**{f'{title_param}__icontains': title_query}))

        return CategoryModel.objects.all()
    
    
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            product = get_object_or_404(CategoryModel, id=kwargs['pk'])
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
        instance = CategoryModel.objects.get(id=category_id)

        serializer = CategorySerializer(instance)

        serializer_data = serializer.data
        serializer_data.update(request.data)

        serializer = CategorySerializer(instance, data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "category was deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
