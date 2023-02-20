from django.db import models

# Create your models here.
class Comment(models.Model):
    groupId = models.BigIntegerField()
    userId = models.BigIntegerField()
    comment = models.CharField(max_length=500)
    createdAt = models.DateTimeField()
