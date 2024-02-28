from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import yasg


urlpatterns = [
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path("admin/", admin.site.urls),
    path("api/", include('api.urls')),
] + yasg.urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)