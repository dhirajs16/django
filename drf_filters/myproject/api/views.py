from django.shortcuts import render
from rest_framework import viewsets 
# from .filters import StudentFilters #with global filter setting in settings.py
from rest_framework.filters import SearchFilter
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # filterset_class = StudentFilters
    
    filter_backends = [SearchFilter] # For search filter
    # search_fields = ['name', 'checked_by', 'subject'] # For multiple attribute searching
    search_fields = ['^name']
    