from comment.models import Comment
from django.http import JsonResponse, Http404
from comment.serializers import CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def comments(request):
    if request.method == 'GET':
        data = Comment.objects.all()
        serializer = CommentSerializer(data, many=True)
        return Response({'comments': serializer.data})
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'comment': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST', 'DELETE'])
def comment(request, id):
    try:
        data = Comment.objects.get(pk=id)
    except Comment.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(data)
        return Response({'comment': serializer.data})

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'comment': serializer.data})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
