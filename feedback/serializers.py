from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'group', 'user', 'like', 'dislike', 'details', 'created_at']
        depth = 3