from users.models import User
from group.models import Group
from category.models import Category
from django.http import JsonResponse, Http404
from users.serializers import UserSerializer
from group.serializers import GroupSerializer
from category.serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import numpy as np
from itertools import chain
from sklearn.metrics.pairwise import cosine_similarity


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
        if group in user.groups.all():
            return Response("Already a member of this group")
        user.groups.add(group)
    if request.method == 'DELETE':
        if group not in user.groups.all():
            return Response("Not a member of this group")
        user.groups.remove(group)
    serializer = UserSerializer(user)
    return Response({'user': serializer.data})
    
    
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
        if category in user.categories.all():
            return Response("Already have this category")
        user.categories.add(category)
    elif request.method == 'DELETE':
        if category not in user.categories.all():
            return Response("No category to remove")
        user.categories.remove(category)
    serializer = UserSerializer(user)
    return Response({'user': serializer.data})

@api_view(['GET',])
def view_user_groups(request, userid):
    try:
        user = User.objects.get(pk=userid)
    except User.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = user.groups
        serializer = GroupSerializer(data, many=True)
        return Response({'groups': serializer.data})
    
@api_view(['GET',])
def view_user_categories(request, userid):
    try:
        user = User.objects.get(pk=userid)
    except User.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = user.categories
        serializer = CategorySerializer(data, many=True)
        return Response({'categories': serializer.data})
    
#reshape vectors to have 1 row for a single sample
def cosine_similarity_list(list1, list2):
    list1 = list1.reshape(1,-1)
    list2 = list2.reshape(1,-1)
    return cosine_similarity(list1, list2)[0][0]

def create_index_map(categories):
    category_map = {}
    for index, category in enumerate(categories):
        category_map[category.id] = index
    return category_map

def group_recommend(user, groups, N=5):
    # get list of unique categories from the groups
    categories = set(chain.from_iterable([group.categories.all() for group in groups]))

    category_map = create_index_map(categories)

    # convert categories data (one-hot encoding)
    group_category_vectors = []
    for group in groups:
        vector = np.zeros(len(categories))
        for category in group.categories.all():
            vector[category_map[category.id]] = 1
        group_category_vectors.append(vector)

    # convert user data (one-hot encoding)
    user_category_vector = np.zeros(len(categories))
    for category in user.categories.all():
        try:
            user_category_vector[category_map[category.id]] = 1
        except KeyError:
            # Handle the case where the key is not found or print a message for debugging
            print(f"Category ID {category.id} not found in category_map")

    #calculate similarity
    similarity_scores = [cosine_similarity_list(user_category_vector, group_vector) for group_vector in group_category_vectors]

    # sort
    sorted_groups = np.argsort(similarity_scores)[::1]

    rec_groups = [groups[int(index)] for index in sorted_groups[:N]]

    return rec_groups

@api_view(['GET'])
def create_rec_list(request, userid):
    try:
        user = User.objects.get(pk=userid)
    except User.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        user = User.objects.get(pk=userid)
        list = Group.objects.all()
        filtered_groups = list.filter(city=user.city)
        recomended_groups = group_recommend(user, filtered_groups, N=5)
        serializer = GroupSerializer(recomended_groups, many=True)
        return Response({'groups': serializer.data})