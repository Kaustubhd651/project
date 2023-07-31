# views.py
from django.shortcuts import render, get_object_or_404
from .models import Student, Marks, Teacher, Subject

def input_marks(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        teacher_id = request.POST['teacher_id']
        subject_id = request.POST['subject_id']
        marks = request.POST['marks']

        # save the marks into the database
        marks_obj = Marks(student_id=student_id, teacher_id=teacher_id, subject_id=subject_id, marks=marks)
        marks_obj.save()

    students = Student.objects.all()
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'input_marks.html', {'students': students, 'teachers': teachers, 'subjects': subjects})

def view_marks(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']

        # fetch marks for the selected student
        marks = Marks.objects.filter(student_id=student_id)

    students = Student.objects.all()
    return render(request, 'view_marks.html', {'students': students})

def view_student_marks(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']

        #  fetch marks for the selected student and teacher details
        marks = Marks.objects.filter(student_id=student_id)
        student = Student.objects.get(pk=student_id)
        teacher = Teacher.objects.get(pk=marks[0].teacher_id)

    students = Student.objects.all()
    return render(request, 'view_student_marks.html', {'students': students})
