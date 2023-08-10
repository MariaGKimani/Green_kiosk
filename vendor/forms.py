from django import forms
from .models import Vendor


class VendoruploadForm(forms.ModelForm):
    class Meta :      
       model = Vendor                 # model to create our form for products
       fields = "__all__"