# Generated by Django 5.0.1 on 2024-03-22 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_contactform_alter_blogmodel_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactForm',
            new_name='ContactFormModel',
        ),
    ]
