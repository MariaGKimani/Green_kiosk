from django.db import models
from django.contrib.auth.models import User
from Order.models import Order
# Create your models here.
class Customer(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    orderr = models.ForeignKey(Order,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    email = models.CharField(max_length=32)
    address = models.TextField()
    password= models.CharField(max_length=32)
    confirm_password = models.CharField(max_length=32)
    
    
    def __str__(self):
        return f" {self.first_name}  {self.last_name}"

