from django.shortcuts import render
from http.client import HTTPResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from users.serializers import UserSerializer
from django.contrib.auth import authenticate
import json
import pdb; 

from category.models import Category
from group.models import Group
from users.models import User

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_category = Category.objects.all().count()
    num_group = Group.objects.all().count()
    num_user = User.objects.all().count()

    context = {
        'num_category': num_category,
        'num_group': num_group,
        'num_user': num_user
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

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
     