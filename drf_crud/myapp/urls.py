from django.urls import path
from . import views

urlpatterns = [
    path('', views.CLStudentInfo.as_view(), name='CLStudentInfo'),
    path('<int:pk>/', views.RUDStudentInfo.as_view(), name='RUDStudentInfo'),
]