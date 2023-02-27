from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.users, name='users'),
    path('api/user/<int:id>', views.user, name='user'),
    path('api/signup/', views.signup, name='signup'),
]
