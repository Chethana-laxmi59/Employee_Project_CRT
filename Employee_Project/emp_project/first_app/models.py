from django.db import models


# Create your models here.

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=55)
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    designation = models.CharField(max_length=100, default="Unknown")
    emp_type = models.CharField(max_length=100, default="Unknown")
    salary = models.IntegerField(null=True, blank=True)


from django.db import models

# Create your models here.
