from django.urls import path
# from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.log_out, name='logout'),
    path('login/', views.log_in, name='login'),
    # path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]