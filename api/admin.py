from django.contrib import admin
from .models import (
    ProductModel, 
    ProductCategoryModel,
    BlogModel,
    BlogCategoryModel,
    ContactFormModel,
    FormProductsModel,
    ContactFormModel,
    ProductFormModel
)


admin.site.register(ProductModel)
admin.site.register(ProductCategoryModel)
admin.site.register(BlogModel)
admin.site.register(BlogCategoryModel)
admin.site.register(ContactFormModel)
admin.site.register(FormProductsModel)
admin.site.register(ProductFormModel)