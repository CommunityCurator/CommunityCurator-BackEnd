from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_city = models.CharField(max_length=50)
    event_state = models.CharField(max_length=50)
    event_description = models.CharField(max_length=500)
    event_categories = models.ManyToManyField('category.Category', blank=True, related_name='category_events')
    event_image = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    event_creator = models.ForeignKey('users.User', related_name='created_events', on_delete=models.CASCADE)