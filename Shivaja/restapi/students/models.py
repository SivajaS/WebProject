from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    place=models.CharField(max_length=30)

def __str__(self):
    return self.name
    