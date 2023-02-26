from rest_framework import serializers
from .models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'group_name', 'description', 'city', 'state', 'image', 'created_at' , 'categories', 'users']
        depth = 2