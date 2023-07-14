from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.TextField(null=True, blank=True)