from django.urls import path
from . import views

urlpatterns=[
    path ('api/post/', views.posts, name='posts'),
    path ('api/post/<int:id>', views.post, name='post'),
]