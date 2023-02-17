from users.models import User
from django.http import JsonResponse, Http404
from users.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        data = User.objects.all()
        serializer = UserSerializer(data, many=True)
        return Response({'users': serializer.data})
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST', 'DELETE'])
def user(request, id):
    try:
        data = User.objects.get(pk=id)
    except User.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(data)
        return Response({'user': serializer.data})

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user': serializer.data})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
def signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully registered a new user."
            data['email'] = user.email
            data['username'] = user.userName
        else:
            data = serializer.errors
        return Response(data)