
from django.shortcuts import render, redirect
from app.models import *
# Create your views here.
def library(request): 
    # retrieve books in the library
    books = LibraryBook.objects.all()
    # render the library page
    return render(request, 'library.html', {'books': books})
def assignments(request):
    # retrieve the assignments
    assignments = Assignment.objects.all()
    # render the assignments page
    return render(request, 'assignments.html', {'assignments': assignments})
def notifications(request):
    return render(request, 'notifications.html')
def profile(request):
    return render(request, 'profile.html')
def about(request):
    return render(request, 'about.html')

from django.shortcuts import render, redirect
from app.models import *
# Create your views here.
def library(request): 
    # retrieve books in the library
    books = LibraryBook.objects.all()
    # render the library page
    return render(request, 'library.html', {'books': books})
def assignments(request):
    # retrieve the assignments
    assignments = Assignment.objects.all()
    # render the assignments page
    return render(request, 'assignments.html', {'assignments': assignments})
def notifications(request):
    return render(request, 'notifications.html')
def profile(request):
    return render(request, 'profile.html')

