from django.urls import path
from . import views

urlpatterns=[
    path ('api/groups/', views.groups, name='groups'),
    path ('api/group/<int:id>', views.group, name='group'),
    path ('api/groups/<city>', views.group_city, name='group_city'),
    path ('api/groups/<city>/<int:joined_users>', views.group_city_user, name='group_city_user'),
    path ('api/groups/cat/<categories>', views.group_category, name='group_category'),
    path ('api/groups/cat/<categories>/<int:joined_users>', views.group_category_user, name='group_category_user')
]