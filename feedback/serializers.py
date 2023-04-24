from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Feedback
        fields = ['id', 'group', 'user', 'like', 'dislike', 'created_at']
        depth = 2

class LikeSerializer(serializers.ModelSerializer):
    count_like = serializers.IntegerField(read_only=True) 
    
    class Meta:
        model = Feedback
        fields = ['id', 'count_like']

class DislikeSerializer(serializers.ModelSerializer):
    count_dislike = serializers.IntegerField(read_only=True) 
    
    class Meta:
        model = Feedback
        fields = ['id', 'count_dislike']
        


