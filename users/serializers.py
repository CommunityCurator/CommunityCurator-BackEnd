from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name', 'id', 'first_name', 'last_name', 'email',
                  'password',  'bio', 'image', 'created_at', 'groups', 'city', 'state',] #'zipcode',
        depth = 2

class SignUp(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = [
            'user_name', 
            'email',
            'first_name',
            'last_name',
            'password',
            'password2',
            'city',
            'state',
            #'zipcode',
        ]
        depth = 2
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            user_name=self.validated_data['user_name'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            city=self.validated_data['city'],
            state=self.validated_data['state'],
            #zipcode=self.validated_data['zipcode'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user