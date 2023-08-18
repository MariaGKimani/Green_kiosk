# Generated by Django 4.2.3 on 2023-08-14 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_relatedproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='related_product',
            field=models.ManyToManyField(through='inventory.RelatedProduct', to='inventory.product'),
        ),
    ]