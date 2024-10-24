from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentAPIView.as_view(), name='StudentAPIView'),
    path('api/<int:id>/', views.StudentInfo.as_view(), name='StudentInfo'),
]