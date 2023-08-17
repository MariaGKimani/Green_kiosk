from django import forms
from .models import Notification
class NotificationuploadForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = "__all__"