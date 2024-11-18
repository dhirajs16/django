from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# home page view
def index(request):
    return render(request, 'myapp/index.html')

# signup view
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/login/')
        else:
            form = SignupForm()
    else:
        return redirect('/profile/')
    return render(request, 'myapp/signup.html', {'form':form})

# login view
def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request, data = request.POST )
            uname = request.POST.get('username').strip()
            upass = request.POST.get('password')
            
            user = authenticate(username = uname, password = upass)
            
            if user is not None:
                login(request, user)
                return redirect('/profile/')
                
        else:
            form = AuthenticationForm()
    else:
        return redirect('/profile/')
    return render(request, 'myapp/login.html', {'form':form})


# user dashboard view
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'myapp/profile.html', {'user': request.user})
    else:
        return redirect('/login/')
     
     
# logout view   
def log_out(request):
    logout(request)
    return redirect('/login/')
            

# PasswordChangeForm with old password view
def changepassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                return redirect('/login/')
        else:
            form = PasswordChangeForm(user = request.user)
        return render(request, 'myapp/changepass.html', {'form':form})
    else:
        return redirect('/login/')
    
    
# change password without old password view
def changepassword2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('/login/')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'myapp/changepass2.html', {'form':form})
    else:
        return redirect('/login/')