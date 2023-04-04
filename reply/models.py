from django.db import models
from comment.models import Comment
from users.models import User

# Create your models here.
class Reply(models.Model):
    comment = models.ForeignKey(Comment , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_at']
