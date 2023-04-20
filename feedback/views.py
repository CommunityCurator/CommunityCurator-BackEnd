from feedback.models import Feedback
from django.http import JsonResponse, Http404
from feedback.serializers import FeedbackSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count

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
    
@api_view(['POST'])
def new_like(request):
    if request.method == 'POST':
        data = json.loads(request.body) 
        group_id = data.get('group')
        user_id = data.get('user')
        like = data.get('like')

        group = Group.objects.get(id=group_id)
        user = User.objects.get(id=user_id)   

        feedback = Feedback(group=group, user=user, like=like)
        feedback.save()

        response = serializers.serialize('json', [feedback])
        return JsonResponse(response, safe=False, status=201)
    else:
        return JsonResponse(response, safe=False, status=201)

@api_view(['POST'])
def new_dislike(request):
    if request.method == 'POST':
        data = json.loads(request.body) 
        group_id = data.get('group')
        user_id = data.get('user')
        dislike = data.get('dislike')
        detail = data.get('detail')

        group = Group.objects.get(id=group_id)
        user = User.objects.get(id=user_id)   

        feedback = Feedback(group=group, user=user, dislike=dislike, detail=detail)
        feedback.save()

        response = serializers.serialize('json', [feedback])
        return JsonResponse(response, safe=False, status=201)
    else:
        return JsonResponse(response, safe=False, status=201)

@api_view(['GET'])
def group_feedback_count(request, id):
    try:
        data = Feedback.objects.filter(group__id=id).annotate(likes=Count('like'))
    except Feedback.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FeedbackSerializer(data, many=True)
        return Response({'feedbacks': serializer.data})