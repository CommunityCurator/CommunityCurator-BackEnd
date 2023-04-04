from users.models import User
from group.models import Group
from category.models import Category
from django.http import JsonResponse, Http404
from users.serializers import UserSerializer
from group.serializers import GroupSerializer
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
            data['user_name'] = user.user_name
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            data['city'] = user.city
            data['state'] = user.state
        else:
            data = serializer.errors
        return Response(data)
    
@api_view(['GET', 'POST', 'DELETE'])
def join_leave_group(request, userid, groupid):
    try:
        user = User.objects.get(pk=userid)
    except User.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)
    try:
        group = Group.objects.get(pk=groupid)
    except Group.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        user.groups.add(group)
    if request.method == 'DELETE':
        user.groups.remove(group)
    serializer = GroupSerializer(group)
    return Response({serializer.data})
    
@api_view(['GET', 'POST', 'DELETE'])
def add_remove_categories(request, userid, categoryid):
    try:
        user = User.objects.get(pk=userid)
    except User.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)
    try:
        category = Category.objects.get(pk=categoryid)
    except Category.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        user.categories.add(category)
    elif request.method == 'DELETE':
        user.categories.remove(category)
    serializer = UserSerializer(user)
    return Response({serializer.data})

@api_view(['GET',])
def view_user_groups(request, userid):
    try:
        user = User.objects.get(pk=userid)
    except User.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = GroupSerializer(user.groups, many=True)
        return Response({'groups': serializer.data})
    
@api_view(['GET',])
def view_user_categories(request, userid):
    try:
        user = User.objects.get(pk=userid)
    except User.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response({'categories': serializer.data})