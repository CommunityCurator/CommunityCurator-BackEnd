from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField()
    groups = models.ManyToManyField('group.Group')
    