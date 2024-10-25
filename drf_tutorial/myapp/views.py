# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.response import Response
# from .models import Student
# from .serializers import StudentSerializer

# # GET all and POST
# class StudentAPIView(APIView):
#     def get(self, request):
#         obj = Student.objects.all()
#         serializer = StudentSerializer(obj, many = True)
#         return Response(data = serializer.data, status = status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # GET one, PUT, PATCH, DELETE
# class StudentInfo(APIView):
#     def get(self, request, id):
#         try:
#             obj = Student.objects.get(id = id)

#         except Student.DoesNotExist:
#             msg = {'message': 'Not Found'}
#             return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = StudentSerializer(obj)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, id):
#         try:
#             obj = Student.objects.get(id = id)

#         except Student.DoesNotExist:
#             msg = {'message': 'Not Found'}
#             return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = StudentSerializer(obj, data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def patch(self, request, id):
#         try:
#             obj = Student.objects.get(id = id)

#         except Student.DoesNotExist:
#             msg = {'message': 'Not Found'}
#             return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = StudentSerializer(obj, data = request.data, partial = True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     def delete(self, request, id):
#         try:
#             obj = Student.objects.get(id = id)

#         except Student.DoesNotExist:
#             return Response({'message':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
#         obj.delete()
#         return Response({'message': 'Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)
        











from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer



class StudentInfo(APIView):
    def get(self, request, id):
        try:
            obj = Student.objects.get(id = id)
        except Student.DoesNotExist:
            return Response({'message':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, id):
        try:
            obj = Student.objects.get(id = id)
        except Student.DoesNotExist:
            return Response({'message':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(obj, data = request.data)
        if not serializer.is_valid():
            return Response({'message':'Invalid upadate'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)



    def patch(self, request, id):
        try:
            obj = Student.objects.get(id = id)
        except Student.DoesNotExist:
            return Response({'message':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(obj, data = request.data, partial = True)
        if not serializer.is_valid():
            return Response({'message':'Invalid upadate'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    

    def delete(self, request, id):
        try:
            obj = Student.objects.get(id = id)
        except Student.DoesNotExist:
            return Response({'message': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response({'message':'Deleted Successfully'}, status=status.HTTP_205_RESET_CONTENT)







