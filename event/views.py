from event.models import Event
from django.http import JsonResponse, Http404
from event.serializers import EventSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def events(request):
    if request.method == 'GET':
        data = Event.objects.all()
        serializer = EventSerializer(data, many=True)
        return Response({'events': serializer.data})
    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'event': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST', 'DELETE'])
def event(request, id):
    try:
        data = Event.objects.get(pk=id)
    except Event.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventSerializer(data)
        return Response({'event': serializer.data})

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'POST':
        serializer = EventSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'event': serializer.data})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)