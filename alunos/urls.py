from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.StudentListView.as_view(), name='student-list'),
    # Adicione mais URLs conforme necessário
]
