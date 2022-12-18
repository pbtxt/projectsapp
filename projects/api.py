from projects.models import Project
from projects.models import Student
from projects.models import Grade
from projects.models import Professor
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer
from .serializers import StudentSerializer
from .serializers import GradeSerializer
from .serializers import ProfessorSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = StudentSerializer


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GradeSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProfessorSerializer
