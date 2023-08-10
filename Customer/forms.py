from django import forms
from .models import Customer


class CustomeruploadForm(forms.ModelForm):
    class Meta :
       model = Customer                    # model to create our form for products
       fields = "__all__"