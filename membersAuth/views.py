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

def managesubscribers(request):
    # adding mails to the database
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page or any other desired page
    else:
        form = SubscriberForm()

    return render(request, 'base.html', {'form': form})
    

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




def book_list(request):
    books = LibraryBook.objects.all()
    return render(request, 'filterbytitle.html', {'books': books})





# def add_to_collection(request, book_id):
#     book = LibraryBook.objects.get(id=book_id)

#     # Retrieve or create the collection for the logged-in user
#     collection, created = Collect.objects.get_or_create(user=request.user)

#     # Add the book to the collection
#     collection.books.add(book)

#     return redirect('collection')


def move_user(request, book_id):
    # Retrieve the user from the "User" model
    book_to_move = get_object_or_404(LibraryBook, id=book_id)

    # Create a corresponding entry in the "SelectedUser" model
    collect = Collect.objects.create(books=book_to_move)

    # Optionally, you can delete the user from the "User" model if needed
    # user_to_move.delete()
    

    return redirect('filterbytitle')  # Redirect to a page displaying the list of users
