from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = StudentSerializer

    #course
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    #announcement
class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    #assignment
class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    #library book
class LibraryBookViewSet(viewsets.ModelViewSet):
    queryset = LibraryBook.objects.all()
    serializer_class = LibraryBookSerializer


