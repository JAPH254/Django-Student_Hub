# accounts/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView, DeleteView
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
from app.models import *

def register(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')
        
        else:
            form = CreateUserForm()
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
    

# # updating the user information
def update_profile(request):
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserForm(instance=request.user)
    return render(request, 'update_profile.html', {'form': form})

def add_to_collection(request, book_id):
    book = get_object_or_404(LibraryBook, pk=book_id)
    user_collection, created = Collection.objects.get_or_create(user=request.user)
    user_collection.books.add(book)
    return redirect('bookscollected')  # Redirect to your book listing page

class CollectionListView(ListView):
    model = Collection
    template_name = 'collection.html'

    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)

class BookDeleteView(DeleteView):
    model = LibraryBook
    template_name = 'book_confirm_delete.html'
    success_url = '/collection/'  # Redirect to your collection page