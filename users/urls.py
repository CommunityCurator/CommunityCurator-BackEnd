from django.urls import path
from . import views
from .views import(
    signup,
    )

app_name = "user"

urlpatterns = [
    path('api/users/', views.users, name='users'),
    path('api/signup/', views.signup, name='signup'),
]
