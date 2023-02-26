from django.db import models

# Create your models here.
class Reply(models.Model):
    comment_id = models.ForeignKey('reply.Reply')
    user_id = models.OneToOne('users.User')
    reply = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
