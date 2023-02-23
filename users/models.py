from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    bio = models.CharField(max_length=500)
    image = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    groups = models.ManyToManyField('group.Group')

