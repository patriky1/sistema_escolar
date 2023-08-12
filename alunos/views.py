from django.shortcuts import render
from django.views import generic
from .models import Student

class StudentListView(generic.ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
