from django.contrib import admin
from .models import (
    ProductModel, 
    ProductCategoryModel,
    BlogModel,
    BlogCategoryModel,
    FormModel,
    FormProductsModel
)


admin.site.register(ProductModel)
admin.site.register(ProductCategoryModel)
admin.site.register(BlogModel)
admin.site.register(BlogCategoryModel)
admin.site.register(FormModel)
admin.site.register(FormProductsModel)