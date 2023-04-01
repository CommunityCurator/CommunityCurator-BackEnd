from django.urls import path
from . import views
from .views import SearchGroupList

urlpatterns=[
    path ('api/groups/', views.groups, name='groups'),
    path ('api/group/<int:id>', views.group, name='group'),
    path ('api/searchgroups/', SearchGroupList.as_view(), name='search_group_list'),
]