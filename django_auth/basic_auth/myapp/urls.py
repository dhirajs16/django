from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('changepassword2/', views.changepassword2, name='changepassword2'),
]