from django.db import models
from category.models import Category
from users.models import User


# Create your models here.
class Group(models.Model):
    group_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank = True)
    image = models.CharField(max_length=100, blank = True)
    created_at = models.DateTimeField()
    categories = models.ManyToManyField(Category)
    users = models.ManyToManyField(User)
