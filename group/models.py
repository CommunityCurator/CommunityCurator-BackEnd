from django.db import models
from category.models import Category

# Create your models here.
class Group(models.Model):
    groupName = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    categories = models.ManyToManyField(Category)
