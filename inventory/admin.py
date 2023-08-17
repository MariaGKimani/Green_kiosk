from django.contrib import admin
# Register your models here.
from .models import Product,RelatedProduct
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','stock' ,'price' ,'date_created','description')
admin.site.register(Product,ProductAdmin)
admin.site.register(RelatedProduct)
