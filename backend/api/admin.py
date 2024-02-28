from django.contrib import admin
from .models import ProductModel, CategoryModel


admin.site.register(ProductModel)
admin.site.register(CategoryModel)