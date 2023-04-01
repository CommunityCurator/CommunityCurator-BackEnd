from group.models import Group
from django.http import JsonResponse, Http404
from django.db.models import Q
from group.serializers import GroupSerializer
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def groups(request):
    if request.method == 'GET':
        data = Group.objects.all()
        serializer = GroupSerializer(data, many=True)
        return Response({'groups': serializer.data})
    elif request.method == 'POST':
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'group': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST', 'DELETE'])
def group(request, id):
    try:
        data = Group.objects.get(pk=id)
    except Group.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupSerializer(data)
        return Response({'group': serializer.data})

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'POST':
        serializer = GroupSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'group': serializer.data})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class SearchGroupList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['city', 'categories', 'group_name']
    ordering_fields = ['group_name']

    def get_queryset(self):
        queryset = Group.objects.all()
        city = self.request.query_params.get('city', None)
        categories = self.request.query_params.get('categories', None)
        group_name = self.request.query_params.get('group_name', None)
        if city is not None:
            queryset = queryset.filter(city=city)
        if categories is not None:
            queryset = queryset.filter(categories=categories)
        if group_name is not None:
            queryset = queryset.filter(group_name__icontains=group_name)
        return queryset
    
    #Beginning of a suggestion rest call, not yet fully implemented
class SuggestGroupList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['city', 'categories', 'joined_users', 'joined_users.categories']
    ordering_fields = ['group_name']
    def get_queryset(self):
        queryset = Group.objects.all()
        city = self.request.query_params.get('city', None)
        categories = self.request.query_params.get('categories', None)
        group_name = self.request.query_params.get('group_name', None)
        if city is not None:
            queryset = queryset.filter(city=city)
        if categories is not None:
            queryset = queryset.filter(categories=categories)
        return queryset