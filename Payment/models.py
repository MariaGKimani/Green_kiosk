from django.db import models

# Create your models here.
class  Payment(models.Model):
    amount = models.FloatField()
    # payment_method = models.CharField(max_length= 32)
    date =models.DateField()
    # receipt = models.TextField()
    status = models.CharField(max_length = 32)
    # order = models.TextField()
    
    def __str__(self):
        return  self.status