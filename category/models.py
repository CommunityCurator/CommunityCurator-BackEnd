from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    created_at = models.DateField()