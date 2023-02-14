from django.db import models

# Create your models here.


class User(models.Model):
    userName = models.CharField(max_length=30)
    firstName = models.CharField(max_length=35)
    lastName = models.CharField(max_length=35)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    bio = models.CharField(max_length=500)
    image = models.CharField(max_length=100)
    createdAt = models.DateField()

