from django.db import models
from group.models import Group
from users.models import User

# Create your models here.

class Feedback(models.Model):
    group = models.ForeignKey(Group, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    like = models.BooleanField()
    dislike = models.BooleanField()
    report = models.BooleanField()
    details = models.TextField(max_length=250, blank=True)
    created_at= models.DateTimeField(auto_now_add=True)

