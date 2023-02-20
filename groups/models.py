from django.db import models

# Create your models here.
class Group(models.Model):
    groupName = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=True)
    image = models.CharField(max_length=100, blank=True)
    createdAt = models.DateField(blank=True)