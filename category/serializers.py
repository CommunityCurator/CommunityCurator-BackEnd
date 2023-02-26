from group.serializers import GroupSerializer
from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        model = Category
        fields = ['name', 'created_at', 'groups']
        depth = 2