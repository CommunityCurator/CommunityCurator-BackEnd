from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=20)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    image = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField('group.Group', blank=True)

