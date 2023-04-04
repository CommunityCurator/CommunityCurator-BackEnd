from django.db import models
from group.models import Group
from users.models import User

# Create your models here.

class Post(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_at']
