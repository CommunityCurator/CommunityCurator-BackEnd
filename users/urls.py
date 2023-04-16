from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.users, name='users'),
    path('api/user/<int:id>', views.user, name='user'),
    path('api/signup/', views.signup, name='signup'),
    path('api/user/<int:userid>/groups/<int:groupid>', views.join_leave_group, name='join_leave_group'),
    path('api/user/<int:userid>/categories/<int:categoryid>', views.add_remove_categories, name='add_remove_categories'),
    path('api/user/<int:userid>/groups/', views.view_user_groups, name='view_user_groups'),
    path('api/user/<int:userid>/categories/', views.view_user_categories, name='view_user_categories'),
    path('api/recommended/<int:userid>/', views.create_rec_list, name='view_create_rec_list'),
]
