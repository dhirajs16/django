from django.shortcuts import render
from rest_framework import viewsets 
# from .filters import StudentFilters #with global filter setting in settings.py
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    
    # 1. Searching
    # filterset_class = StudentFilters
    # filter_backends = [SearchFilter] # For search filter
    # search_fields = ['name', 'checked_by', 'subject'] # For multiple attribute searching
    # search_fields = ['^name'] # for all the name starting with a particular letter
    
    # 2. Sorting/Ordering
    # filter_backends = [OrderingFilter]
    # ordering_fields = ['name']
    
    # 3. Both searching and sorting together
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'roll', 'checked_by', 'subject']
    
    

"""
NOTE: If we don't use ordering_fields = [], the filter option in the browser will show options
    to sort as per all the fields/attritutes of the table. 
    But if we don't apply search_fields for the SearchFilter, the option of searching the data
    will not appear.
    
    While descending ordering, the ordering params is like ordering=-name.
"""
    
    