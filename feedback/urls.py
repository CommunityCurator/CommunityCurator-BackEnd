from django.urls import path
from . import views

urlpatterns=[
    path ('api/feedback/', views.feedbacks, name='feedbacks'),
    path ('api/feedback/<int:id>', views.feedback, name='feedback'),
] 