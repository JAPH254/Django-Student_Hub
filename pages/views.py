
from django.shortcuts import render, redirect
from app.models import *
from .forms import *
from app.filters import *
# Create your views here.
def filterbytitle(request): 
    book_list = LibraryBook.objects.all()
    book_filter = BookFilterbytitle(request.GET, queryset=book_list)
    return render(request, 'filterbytitle.html', {'filter': book_filter})
def filterbyauthor(request): 
    book_list = LibraryBook.objects.all()
    book_filter = BookFilterbyauthor(request.GET, queryset=book_list)
    return render(request, 'filterbyauthor.html', {'filter': book_filter})
def filterbyISBN(request): 
    book_list = LibraryBook.objects.all()
    book_filter = BookFilterbyISBN(request.GET, queryset=book_list)
    return render(request, 'filterbyISBN.html', {'filter': book_filter})
def assignments(request):
    # retrieve the assignments
    assignments = Assignment.objects.all()
    # render the assignments page
    return render(request, 'assignments.html', {'assignments': assignments})
def notifications(request):
    return render(request, 'notifications.html')
def profile(request):
    print(request.user.profile_picture)
    print(request.user.phone_number)
    return render(request, 'profile.html', {'user': request.user})

def about(request):
    return render(request, 'about.html')
def library(request):
    return render(request, 'library.html')

from django.shortcuts import render, redirect
from app.models import *
def assignments(request):
    # retrieve the assignments
    assignments = Assignment.objects.all()
    # render the assignments page
    return render(request, 'assignments.html', {'assignments': assignments})
def notifications(request):
    return render(request, 'notifications.html')
def profile(request):
    return render(request, 'profile.html')

def infopage(request):
    return render(request, 'infopage.html')
def collection(request):
    return render(request, 'collection.html')


def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            book = LibraryBook.objects.filter(title__contains=query) 
            return render(request, 'search.html', {'book':book})
        else:
            print("No information to show")
            return render(request, 'search.html', {})