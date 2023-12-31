# Generated by Django 4.2.3 on 2023-08-14 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
                ('related_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_products', to='inventory.product')),
            ],
        ),
    ]
