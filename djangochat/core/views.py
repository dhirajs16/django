from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
        
    else:
        form = SignupForm

    return render(request, 'core/signup.html', {'form':form})


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        uname = request.POST.get('username').strip()
        upass = request.POST.get('password1')
        user = authenticate(username = uname, password = upass)
        if user is not None:
            login(request, user)
            return redirect('frontpage')
        
    else:
        form = AuthenticationForm()

    return render(request, 'core/login.html', {'form': form})


@login_required
def log_out(request):
    logout(request)
    return redirect('frontpage')