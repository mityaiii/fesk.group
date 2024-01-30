from django.urls import path
from . import views


urlpatterns = [
    path('products', views.ProductView.as_view(), name="products"),
    path('products/<int:pk>', views.ProductView.as_view(), name="products-by-id"),
    path('categories', views.CategoryView.as_view(), name="caregories-by-id"),
    path('categories/<int:pk>', views.CategoryView.as_view(), name="caregories-by-id"),
]