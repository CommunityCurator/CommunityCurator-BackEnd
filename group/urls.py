from django.urls import path
from . import views

urlpatterns=[
    path ('', views.groups, name='groups'),
    path ('<int:id>', views.group, name='group'),
    path ('<city>', views.group_city, name='group_city'),
    path ('<city>/<int:userid>', views.group_city_user, name='group_city_user'),
    path ('<category>', views.group_category, name='group_category'),
    path ('<category>/<int:userid>', views.group_category_user, name='group_category_user')
]