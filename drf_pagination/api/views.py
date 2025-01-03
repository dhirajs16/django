from django.shortcuts import render
from rest_framework import viewsets
from .paginations import MyPageNumberPagination, MyLimitOffsetPagination
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyLimitOffsetPagination