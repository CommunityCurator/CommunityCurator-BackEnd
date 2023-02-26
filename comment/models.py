from django.db import models

# Create your models here.
class Comment(models.Model):
    group_id = models.OneToOne('group.Group')
    user_id = models.OneToOne('users.User')
    comment = models.CharField(max_length=500)
    replies = models.ForeignKey('reply.Reply')
    created_at = models.DateTimeField(auto_now_add=True)
