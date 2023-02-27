from django.db import models
from group.models import Group
from users.models import User

# Create your models here.
class Comment(models.Model):
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
