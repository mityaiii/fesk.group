# Generated by Django 5.0.1 on 2024-03-01 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_productcategorymodel_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formmodel',
            options={'verbose_name_plural': 'Формы'},
        ),
        migrations.AlterModelOptions(
            name='formproductsmodel',
            options={'verbose_name_plural': 'Формы с продуктами'},
        ),
    ]
