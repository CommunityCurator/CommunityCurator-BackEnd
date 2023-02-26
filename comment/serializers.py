from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'group_id', 'user_id', 'comment', 'created_at']