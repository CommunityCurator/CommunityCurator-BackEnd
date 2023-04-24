import json
from group.models import Group
from users.models import User
from feedback.models import Feedback
from django.http import JsonResponse, Http404
from feedback.serializers import FeedbackSerializer, LikeSerializer, DislikeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from datetime import date


@api_view(['GET', 'POST'])
def feedbacks(request):
    
    if request.method == 'GET':
        data = Feedback.objects.all()
        serializer = FeedbackSerializer(data, many=True)
        return Response({'feedbacks': serializer.data})
    elif request.method == 'POST':
        

        # added code - was not able to use the serializer to implement to add functionality. Borrowered from the update new_like method beginning on 67 to get this post action to work.
        print(request.data["user"])
        group = Group.objects.get(id=request.data["group"])
        user = User.objects.get(id=request.data["user"])   

        feedback = Feedback(group=group, user=user, like=request.data["like"], dislike=request.data["dislike"], report=request.data["report"], created_at= request.data["created_at"])
        feedback.save()
         
        # serializer = FeedbackSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({'feedback': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
      

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

        response = feedback.serializers.serialize('json', [feedback])
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

        response = feedback.serializers.serialize('json', [feedback])
        return JsonResponse(response, safe=False, status=201)
    else:
        return JsonResponse(response, safe=False, status=201)

@api_view(['GET'])
def group_like_count(request, id):
    try:
        data = Feedback.objects.filter(group__id=id, like="True") 
        data = data.annotate(count_like=Count('id'))
    except Feedback.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LikeSerializer(data, many=True)
        return Response({'likes': data.count()})

@api_view(['GET'])
def group_dislike_count(request, id):
    try:
        data = Feedback.objects.filter(group__id=id, dislike="True") 
        data = data.annotate(count_dislike=Count('id'))
    except Feedback.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DislikeSerializer(data, many=True)
        return Response({'dislikes': data.count()})