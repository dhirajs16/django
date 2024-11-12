from django.shortcuts import render
from rest_framework import viewsets 
from .filters import StudentFilters
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_class = StudentFilters