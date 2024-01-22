from django.urls import path
from . import views


urlpatterns = [
    path('login', views.sign_in, name="sign in"),
    path('products', views.ProductView.as_view(), name="products"),
    path('products/<int:pk>', views.ProductView.as_view(), name="products-by-id"),
    path('caregories', views.CategoryView.as_view(), name="caregories-by-id"),
    path('caregories/<int:pk>', views.CategoryView.as_view(), name="caregories-by-id"),
]