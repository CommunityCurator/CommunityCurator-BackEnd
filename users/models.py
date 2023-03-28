from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    #zipcode = models.CharField(max_length=12)
    bio = models.CharField(max_length=500, blank=True)
    image = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField('group.Group', blank=True, related_name='joined_groups')
    #suggested_groups = models.ManyToManyField('group.Group', blank=True, related_name='suggested_groups')