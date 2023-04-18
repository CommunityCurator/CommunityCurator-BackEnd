from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'group_id', 'user_id', 'content', 'created_at', 'parent_id' ]
        depth = 3