from django.db import models


class Disciplina(models.Model):
    name = models.CharField(max_length=200)
    carga_horaria = models.CharField(max_length=200)
    nota1 = models.DecimalField(max_digits=5, decimal_places=2)
    nota2 = models.DecimalField(max_digits=5, decimal_places=2)
    nota3 = models.DecimalField(max_digits=5, decimal_places=2)
    nota4 = models.DecimalField(max_digits=5, decimal_places=2)

    def _str_(self) -> str:
        return self.name 

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nota1 = models.ForeignKey(Disciplina.nota1, on_delete=models.CASCADE)
    nota2 = models.ForeignKey(Disciplina.nota2, on_delete=models.CASCADE)
    nota3 = models.ForeignKey(Disciplina.nota3, on_delete=models.CASCADE)
    nota4 = models.ForeignKey(Disciplina.nota4, on_delete=models.CASCADE)
    bimestre = models.CharField(max_length=10)
    
    def _str_(self) -> str:
        return self.first_name + " " + self.last_name

class Turma(models.Model):
    disciplinas = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    students = models.ManyToManyField(Student, through='Enrollment')
    def __str__(self) -> str:
       return self.name
    

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    enrollment_date = models.DateField()

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=5, decimal_places=2)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=True)
    def __str__(self) -> str:
       return self.student

