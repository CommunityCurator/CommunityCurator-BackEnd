from django.urls import path
from . import views

urlpatterns=[
    path ('api/reply/', views.replies, name='replies'),
    path ('api/reply/<int:id>', views.reply, name='reply'),
]