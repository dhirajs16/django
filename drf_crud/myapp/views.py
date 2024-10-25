from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView
from .models import Student
from .serializers import StudentSerializer

# Create and List Operations
class CLStudentInfo(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # List
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    # Create/Post
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

# Retrieve, Update and Destroy
class RUDStudentInfo(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Retrieve
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    # Update
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    # Destroy
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    