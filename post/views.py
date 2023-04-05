from post.models import Post
from django.http import JsonResponse, Http404
from post.serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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
    
