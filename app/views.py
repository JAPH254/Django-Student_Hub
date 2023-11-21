from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
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


# posting the students details

# def student(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         course = request.POST.get('course')
#         year = request.POST.get('year')

#         student = Student(name=name, email=email, phone=phone, course=course, year=year)
#         student.save()
#         return redirect('student')
#     else:
#         return render(request, '')
    