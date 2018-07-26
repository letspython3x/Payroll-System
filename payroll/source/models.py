from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    department = models.CharField(max_length=50)



