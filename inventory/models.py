from django.db import models
from vendor.models import Vendor
# Create your models here.
class Product(models.Model):
    Vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    stock = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    related_product = models.ManyToManyField('self', through='RelatedProduct', symmetrical=False)
    
    
    def __str__(self):
        return  self.name


class RelatedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    related_product = models.ForeignKey(Product, related_name='related_products', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.product.name} -> {self.related_product.name}"
