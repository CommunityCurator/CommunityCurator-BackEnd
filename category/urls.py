from django.urls import path
from . import views

urlpatterns=[
    path ('api/categories/', views.categories, name='categories'),
]