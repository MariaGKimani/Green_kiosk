# Generated by Django 4.2.3 on 2023-08-14 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_product_related_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relatedproduct',
            old_name='related_products',
            new_name='related_product',
        ),
    ]
