from django.urls import path
from . import views

urlpatterns=[
    path ('', views.categories, name='categories'),
    path ('notjoined/<int:userid>', views.not_added_categories, name='not_added_categories'),
]