from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.users, name='users'),
    path('api/users/<int:id>', views.user, name='user'),
]
