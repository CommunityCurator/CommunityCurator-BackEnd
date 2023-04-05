from django.urls import path
from . import views

urlpatterns=[
    path ('api/comment/', views.comments, name='comments'),
    path ('api/comment/<int:id>', views.comment, name='comment'),
]