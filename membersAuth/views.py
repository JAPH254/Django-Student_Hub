# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('sign_in')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

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