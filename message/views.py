from message.models import Message
from django.http import JsonResponse, Http404
from message.serializers import MessageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def messages(request):
    if request.method == 'GET':
        data = Message.objects.all()
        serializer = MessageSerializer(data, many=True)
        return Response({'messages': serializer.data})
    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST', 'DELETE'])
def post(request, id):
    try:
        data = Message.objects.get(pk=id)
    except Message.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MessageSerializer(data)
        return Response({'message': serializer.data})

    # elif request.method == 'DELETE':
    #     data.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'POST':
        print(request.data)
        serializer = MessageSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': serializer.data})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)