

from django.urls import path
from . import views

urlpatterns = [
    path('input-marks/', views.input_marks, name='input_marks'),
    path('view-marks/', views.view_marks, name='view_marks'),
    path('view-student-marks/', views.view_student_marks, name='view_student_marks'),
]
