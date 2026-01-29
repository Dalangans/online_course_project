from django.urls import path
from . import views

app_name = 'online_course'

urlpatterns = [
    # Course URLs
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.course_details, name='course_details'),
    
    # Exam URLs
    path('lessons/<int:lesson_id>/submit/', views.submit, name='submit'),
    path('submissions/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),
]
