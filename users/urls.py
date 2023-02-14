from django.urls import path
from . import views
from .views import(
    registration_view,
    )

app_name = "user"

urlpatterns = [
    path('api/users/', views.users, name='users'),
    #path('api/signup/', registration_view, name='signup'),
]
