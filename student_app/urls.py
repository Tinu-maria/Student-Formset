from django.urls import path
from . import views

urlpatterns = [
    path('students/add', views.add_students, name='add_students'),
    path('students/<int:student_id>/teachers', views.add_teachers, name='add_teachers'),
    
]
