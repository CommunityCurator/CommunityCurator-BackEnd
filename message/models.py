from django.db import models
# from group.models import Group
# from users.models import User

# Create your models here.

class Message(models.Model):
    group_id = models.IntegerField()
    user_id = models.IntegerField()
    content = models.TextField(max_length=500, blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
    parent_id=models.BigIntegerField()
    class Meta:
        ordering=['-created_at']
