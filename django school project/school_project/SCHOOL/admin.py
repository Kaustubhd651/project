# admin.py

from django.contrib import admin
from .models import Student, Teacher, Marks, Subject

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Marks)
admin.site.register(Subject)
