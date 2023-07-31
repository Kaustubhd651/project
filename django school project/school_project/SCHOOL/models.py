# models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    # Add other student-related fields

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    # Add other teacher-related fields

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    # Add other subject-related fields

    def __str__(self):
        return self.name

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    # Add other marks-related fields

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - {self.marks}"
