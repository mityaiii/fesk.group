from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.ProductView.as_view(), name="products"),
    path('products/<int:pk>/', views.ProductView.as_view(), name="products-by-id"),
    path('product-categories/', views.CategoryView.as_view(), name="caregories"),
    path('product-categories/<int:pk>/', views.CategoryView.as_view(), name="caregories-by-id"),
    path('blogs', views.BlogView.as_view(), name="blogs"),
    path('blogs/<int:pk>/', views.BlogView.as_view(), name="blogs-by-id"),
    path('blog-categories/', views.BlogCategoryView.as_view(), name="blog-categories"),
    path('blog-categories/<int:pk>/', views.BlogCategoryView.as_view(), name="blog-categories-by-id"),
    path('forms/', views.BlogCategoryView.as_view(), name="form"),
    path('forms/<int:pk>/', views.BlogCategoryView.as_view(), name="form-by-id"),
    path('form-products/', views.FormProductView.as_view(), name="form-product"),
    path('form-products/<int:pk>/', views.FormProductView.as_view(), name="form-product-by-id"),
]