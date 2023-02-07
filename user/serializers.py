from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userName', 'firstName', 'lastName', 'email',
                  'password', 'bio', 'image', 'created_at']
