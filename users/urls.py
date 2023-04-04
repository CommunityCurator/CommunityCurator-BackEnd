from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.users, name='users'),
    path('api/user/<int:id>', views.user, name='user'),
    path('api/signup/', views.signup, name='signup'),
    path('api/user/<int:id>/groups/<int:group_id>/', views.join_leave_group, name='join_leave_group'),
    path('api/user/<int:id>/categories/<int:category_id>', views.add_remove_categories, name='add_remove_categories'),
    path('api/user/<int:id>/groups/', views.view_user_groups, name='view_user_groups'),
    path('api/user/<int:id>/categories/', views.view_user_categories, name='view_user_categories'),
]
