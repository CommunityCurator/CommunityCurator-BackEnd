from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_location = models.CharField(max_length=50)
    event_description = models.CharField(max_length=500)
    event_image = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    event_creator = models.ForeignKey('users.User', related_name='created_events', on_delete=models.CASCADE)
    #event_groups = models.ManyToManyField('group.Group', blank=True, related_name='group_events')