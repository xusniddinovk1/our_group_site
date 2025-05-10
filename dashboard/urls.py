from django.urls import path
from .views import *

urlpatterns = [
    path('', main_dashboard, name='main_dashboard'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout, name='logout_page'),

    path('subject/list/', subjects_list, name='subjects_list'),
    path('subject/<int:pk>/edit/', update_subject, name='edit_subject'),
    path('subject/<int:pk>/delete/', delete_subject, name='delete_subject'),

    path('teacher/list/', teachers_list, name='teachers_list'),
    path('teacher/<int:pk>/edit/', update_teacher, name='edit_teacher'),
    path('teacher/<int:pk>/delete/', delete_teacher, name='delete_teacher'),

    path('student/list/', students_list, name='students_list'),
    path('student/<int:pk>/edit/', update_student, name='update_student'),
    path('student/<int:pk>/delete/', delete_student, name='delete_student'),

    path('failed_subject/list/', failed_subjects_list, name='failed_subjects_list'),
    path('failed_subject/<int:pk>/edit/', update_failed_subject, name='update_failed_subject'),
    path('failed_subject/<int:pk>/delete/', delete_failed_subject, name='delete_failed_subject'),
]
