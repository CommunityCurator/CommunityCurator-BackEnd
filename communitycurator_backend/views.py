
from http.client import HTTPResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from users.serializers import UserSerializer
from django.contrib.auth import authenticate
import json
import pdb; 


@api_view(['POST'])
def login(request):
  if request.method == 'POST':
    data = json.loads(request.body.decode())
    email = data['email']
    password = data['password']
    if email and password:
      # find email/password combination
      try:
        user = User.objects.get(email=email, password=password)
        serializer = UserSerializer(user)
        return Response({'user': serializer.data})
      except User.DoesNotExist:
        content = {"Error message":"Incorrect email or password'"}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
     