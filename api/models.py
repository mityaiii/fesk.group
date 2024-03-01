from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class ProductCategoryModel(models.Model):
    max_length = 255

    title_ru = models.CharField(max_length=max_length, verbose_name="Название (ru)")
    title_kz = models.CharField(max_length=max_length, verbose_name="Название (kz)")
    title_en = models.CharField(max_length=max_length, verbose_name="Название (en)")

    def __str__(self) -> str:
        return f"{self.title_ru} ({self.title_kz})"
    
    class Meta:
        verbose_name_plural = "Категории продуктов"


class ProductModel(models.Model):
    max_length = 255

    title_ru = models.CharField(max_length=max_length, verbose_name="Название (ru)")
    title_kz = models.CharField(max_length=max_length, verbose_name="Название (kz)")
    title_en = models.CharField(max_length=max_length, verbose_name="Название (en)")

    price_ru = models.FloatField(verbose_name="Цена (руб.)")
    price_kz = models.FloatField(verbose_name="Цена (тенге)")

    description_ru = models.TextField(verbose_name="Описание продукта (ru)")
    description_kz = models.TextField(verbose_name="Описание продукта (kz)")

    image = models.ImageField(upload_to='product_photos/', verbose_name='Фотография', null=True, blank=True)
    category = models.ManyToManyField(ProductCategoryModel, verbose_name="Категории", blank=True)

    def __str__(self) -> str:
        return f'{self.title_ru} ({self.title_kz})'
    
    class Meta:
        verbose_name_plural = "Товары"


class BlogCategoryModel(models.Model):
    max_length = 255

    title_ru = models.CharField(max_length=max_length, verbose_name="Название (ru)")
    title_kz = models.CharField(max_length=max_length, verbose_name="Название (kz)")
    title_en = models.CharField(max_length=max_length, verbose_name="Название (en)")

    def __str__(self) -> str:
        return f"{self.title_ru} ({self.title_kz})"
    
    class Meta:
        verbose_name_plural = "Категории Блог"


class BlogModel(models.Model):
    max_length = 255

    title_ru = models.CharField(max_length=max_length, verbose_name="Название (ru)")
    title_kz = models.CharField(max_length=max_length, verbose_name="Название (kz)")
    title_en = models.CharField(max_length=max_length, verbose_name="Название (en)")

    price_ru = models.FloatField(verbose_name="Цена (руб.)")
    price_kz = models.FloatField(verbose_name="Цена (тенге)")

    description_ru = models.TextField(verbose_name="Короткое описание (ru)")
    description_kz = models.TextField(verbose_name="Короткое описание (kz)")

    content_ru = CKEditor5Field('Text', config_name='extends')
    content_kz = CKEditor5Field('Text', config_name='extends')

    category = models.ManyToManyField(ProductCategoryModel, verbose_name="Категории", blank=True)

    is_public = models.BooleanField(verbose_name="Разместить")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self) -> str:
        return f'{self.title_ru} ({self.title_kz})'
    
    class Meta:
        verbose_name_plural = "Товары"


class FormProductsModel(models.Model):
    product_id = models.ForeignKey(ProductModel, verbose_name="id продкта", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Число")

    class Meta:
        verbose_name_plural = "Формы с продуктами"


class FormModel(models.Model):
    max_length = 255

    fio = models.CharField(verbose_name='ФИО', max_length=max_length)
    telephon = models.CharField(verbose_name='Номер телефона', max_length=20)
    email = models.CharField(verbose_name='Почта', max_length=max_length)
    message = models.TextField(verbose_name='Сообщение', null=True, blank=True)
    products = models.ForeignKey(FormProductsModel, verbose_name="Продукты", null=True, blank=True, on_delete=models.CASCADE)
    # products = models.JSONField(default=dict)
    
    class Meta:
        verbose_name_plural = "Формы"