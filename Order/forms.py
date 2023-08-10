from django import forms
from .models import Order


class OrderuploadForm(forms.ModelForm):
    class Meta :
       model = Order                    # model to create our form for products
       fields = "__all__"