from django.db import models
from post.models import Post
from users.models import User

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_at']