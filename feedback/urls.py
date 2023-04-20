from django.urls import path
from . import views

urlpatterns=[
    path ('api/feedback/', views.feedbacks, name='feedbacks'),
    path ('api/feedback/<int:id>', views.feedback, name='feedback'),
    path ('api/feedback_count/<int:id>', views.group_feedback_count, name='group_feedback_count'),
    path ('api/new_like/', views.new_like, name='new_like'),
    path ('api/new_dislike/', views.new_dislike, name='new_dislike'),
] 