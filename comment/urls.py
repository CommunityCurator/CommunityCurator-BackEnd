from django.urls import path
from . import views

urlpatterns=[
    path ('', views.comments, name='comments'),
    path ('<int:id>', views.comment, name='comment'),
]