# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
# from .forms import *
from app.models import *

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        username = request.POST['username']
        password = request.POST['password']

    # creating the user
        user = User.objects.create_user(username=username, password=password, email=email, first_name=name)
        user.save()
        
        return redirect('sign_in')
    else:
        return render(request, 'register.html')
    

def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'sign_in.html', {'form': form})

def sign_out(request):
    logout(request)
    return redirect('sign_in')
    

# pages views
def assignments(request):
    return render(request, 'assignments.html')
def library(request):
    return render(request, 'library.html')
def notifications(request):
    return render(request, 'notifications.html')
def profile(request):
    return render(request, 'profile.html')