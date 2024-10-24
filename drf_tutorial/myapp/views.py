from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


class StudentAPIView(APIView):
    def get(self, request):
        obj = Student.objects.all()
        serializer = StudentSerializer(obj, many = True)
        return Response(data = serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
