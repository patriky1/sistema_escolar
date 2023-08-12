from django.contrib import admin
from .models import Student, Turma, Enrollment, Grade, Attendance, Disciplina

admin.site.register(Student)
admin.site.register(Turma)
admin.site.register(Enrollment)
admin.site.register(Grade)
admin.site.register(Attendance)
admin.site.register(Disciplina)
