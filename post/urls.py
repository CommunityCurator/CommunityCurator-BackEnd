from django.urls import path
from . import views

urlpatterns=[
    path ('api/post/', views.posts, name='posts'),
    path ('api/post/<int:id>', views.post, name='post'),
    path ('api/posts/<int:id>', views.group_posts, name='group_posts'),
    path ('api/new_post/', views.new_post, name='new_post'),
]