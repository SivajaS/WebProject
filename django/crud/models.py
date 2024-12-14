from django.db import models

# Create your models here.
class Register(models.Model):
    email=models.EmailField(null=True,blank=True)
    name=models.CharField(max_length=50)
    address=models.TextField(null=True,blank=True)