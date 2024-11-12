from django_filters import rest_framework as filters
from .models import Student

class StudentFilters(filters.FilterSet):
    name = filters.CharFilter(lookup_expr = 'icontains')
    checked_by = filters.CharFilter(lookup_expr = 'icontains')
    
    class Meta:
        model = Student
        fields = ['name', 'checked_by']