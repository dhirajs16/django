from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    
    form = SignupForm()
    return render(request, 'signup.html', {'form': form})