from reply.models import Reply
from django.http import JsonResponse, Http404
from reply.serializers import ReplySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def replies(request):
    if request.method == 'GET':
        data = Reply.objects.all()
        serializer = ReplySerializer(data, many=True)
        return Response({'replies': serializer.data})
    elif request.method == 'POST':
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'reply': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST', 'DELETE'])
def reply(request, id):
    try:
        data = Reply.objects.filter(comment_id=id)
    except Reply.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReplySerializer(data)
        return Response({'reply': serializer.data})

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'POST':
        serializer = ReplySerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'reply': serializer.data})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
