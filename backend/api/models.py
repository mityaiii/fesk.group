from django.db import models


class CategoryModel(models.Model):
    max_length = 255

    title_ru = models.CharField(max_length=max_length, verbose_name="Название (ru)")
    title_kz = models.CharField(max_length=max_length, verbose_name="Название (kz)")

    def __str__(self) -> str:
        return f"{self.title_ru} ({self.title_kz})"
    
    class Meta:
        verbose_name_plural = "Категории"


class ProductModel(models.Model):
    max_length = 255

    title_ru = models.CharField(max_length=max_length, verbose_name="Название (ru)")
    title_kz = models.CharField(max_length=max_length, verbose_name="Название (kz)")

    price_ru = models.FloatField(verbose_name="Цена (руб.)")
    price_kz = models.FloatField(verbose_name="Цена (тенге)")

    description_ru = models.TextField(verbose_name="Описание продукта (ru)")
    description_kz = models.TextField(verbose_name="Описание продукта (kz)")

    image = models.ImageField(upload_to='product_photos/', verbose_name='Фотография', null=True, blank=True)
    category = models.ManyToManyField(CategoryModel, verbose_name="Категории", blank=True)

    def __str__(self) -> str:
        return f'{self.title_ru} ({self.title_kz})'
    
    class Meta:
        verbose_name_plural = "Товары"
