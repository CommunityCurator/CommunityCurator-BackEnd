from django.db import models

# Create your models here.
class Group(models.Model):
    groupName = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
