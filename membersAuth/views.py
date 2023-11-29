# accounts/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView, DeleteView
from django.contrib import messages
from .forms import *
from app.models import *
from django.contrib.auth import get_user_model
# views.py


def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            # Redirect to the profile page after successful update
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'update_profile.html', {'form': form})




def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            
            return redirect('sign_in')  # Redirect to the user's profile or dashboard
    else:
        form = UserRegistrationForm()

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


def request_book(request, book_id):
    book = LibraryBook.objects.get(pk=book_id)  # Replace 'Book' with your actual Book model

    if request.method == 'POST':
        form = BookRequestForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            user = request.user
            BookRequest.objects.create(user=user, book=book, message=message)
            return redirect('filterbytitle', book_id=book_id)  # Redirect to the book detail page
    else:
        form = BookRequestForm()

    return render(request, 'filterbytitle.html', {'form': form, 'book': book})

User = get_user_model()
def chat(request, username):
    receiver = User.objects.get(username=username)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = receiver
            message.save()
            return redirect('chat', username=username)
    else:
        form = MessageForm()

    messages = Message.objects.filter(
        (models.Q(sender=request.user) & models.Q(receiver=receiver)) |
        (models.Q(sender=receiver) & models.Q(receiver=request.user))
    ).order_by('timestamp')

    return render(request, 'chat/chat.html', {'receiver': receiver, 'form': form, 'messages': messages})