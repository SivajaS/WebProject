from django.db import models

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)