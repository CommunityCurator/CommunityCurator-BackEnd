from django.urls import path
from . import views

urlpatterns=[
    path ('api/message/', views.messages, name='messages'),
    path ('api/message/<int:id>', views.messages, name='messages'),
]