from rest_framework import serializers

from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_name', 'id', 'event_date', 'event_time', 'event_city', 'event_state', 'event_description', 'event_categories', 'event_image', 'created_at', 'event_creator',] #'event_groups',
        depth = 2