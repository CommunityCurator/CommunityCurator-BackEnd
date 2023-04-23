from django.urls import path
from . import views

urlpatterns=[
    path ('api/feedback/', views.feedbacks, name='feedbacks'),
    path ('api/feedback/<int:id>', views.feedback, name='feedback'),
    #below url pulls the count of likes for a specified group
    path ('api/likes/<int:id>', views.group_like_count, name='group_like_count'),
    #below url pulls the count of dislikes for a specified group
    path ('api/dislikes/<int:id>', views.group_dislike_count, name='group_dislike_count'),
    path ('api/new_like/', views.new_like, name='new_like'),
    path ('api/new_dislike/', views.new_dislike, name='new_dislike'),
] 