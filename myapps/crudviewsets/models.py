from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.name
