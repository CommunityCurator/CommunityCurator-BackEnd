from django.urls import path
from . import views

urlpatterns = [
    path('api/events/', views.event, name='events'),
    path('api/event/<int:id>', views.event, name='event'),
    path('api/signup/', views.signup, name='signup'),
]