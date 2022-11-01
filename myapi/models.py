# models.py
from django.db import models
class Cars(models.Model):
    name = models.CharField(max_length=15)
    brand = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Bike(models.Model):
    name = models.CharField(max_length=15)
    brand = models.CharField(max_length=25)
    def __str__(self):
        return self.name