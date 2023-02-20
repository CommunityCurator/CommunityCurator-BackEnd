from rest_framework import serializers
from .models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'groupName', 'description', 'city', 'state', 'image', 'createdAt' , 'categories', 'users']
        depth = 2