from django.db import models

# Create your models here.
class Comment(models.Model):
    group_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
