from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
# for global authentication use settings.py

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# To Override the global auth and permission settings for this particular class
    authentication_classes = [BasicAuthentication]

# Permission Classes
    # For all registered users(superuser, staff & basic users)
    # permission_classes = [IsAuthenticated]

    # for allowing all permissions (for auth and non-auth user)
    # permission_classes = [AllowAny]

    # If registered then all permissions allowed else can only read data
    # permission_classes = [IsAuthenticatedOrReadOnly]

    # Allowed all permissions for users who are staff
    permission_classes = [IsAdminUser]