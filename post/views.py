import json
from post.models import Post
from django.http import JsonResponse, Http404
from django.core import serializers
from post.serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Group, User

@api_view(['GET', 'POST'])
def posts(request):
    if request.method == 'GET':
        data = Post.objects.all()
        serializer = PostSerializer(data, many=True)
        return Response({'posts': serializer.data})
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'post': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST', 'DELETE'])
def post(request, id):
    try:
        data = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(data)
        return Response({'post': serializer.data})

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'post': serializer.data})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def new_post(request):
    if request.method == 'POST':
        data = json.loads(request.body) 
        group_id = data.get('group')
        user_id = data.get('user')
        content = data.get('content')

        group = Group.objects.get(id=group_id)
        user = User.objects.get(id=user_id)   

        post = Post(group=group, user=user, content=content)
        post.save()

        response = serializers.serialize('json', [post])
        return JsonResponse(response, safe=False, status=201)
    else:
        return JsonResponse(response, safe=False, status=201)

@api_view(['GET'])
def group_posts(request, id):
    try:
        data = Post.objects.filter(group__id=id)
    except Post.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(data, many=True)
        return Response({'posts': serializer.data})