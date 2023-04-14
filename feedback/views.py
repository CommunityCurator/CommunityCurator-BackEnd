from feedback.models import Feedback
from django.http import JsonResponse, Http404
from feedback.serializers import FeedbackSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def feedbacks(request):
    if request.method == 'GET':
        data = Feedback.objects.all()
        serializer = FeedbackSerializer(data, many=True)
        return Response({'feedbacks': serializer.data})
    elif request.method == 'POST':
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'feedback': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST', 'DELETE'])
def feedback(request, id):
    try:
        data = Feedback.objects.get(pk=id)
    except Feedback.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FeedbackSerializer(data)
        return Response({'feedback': serializer.data})

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'POST':
        serializer = FeedbackSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'feedback': serializer.data})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
