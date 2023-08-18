from django.contrib import admin

# Register your models here.
from .models import Payment
class Paymentadmin(admin.ModelAdmin):
    list_display = ('amount','date','status')
admin.site.register(Payment,Paymentadmin)
