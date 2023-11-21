from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    phone = models.CharField(max_length=100, blank=False)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    year = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)
    code = models.CharField(max_length=100, blank=False, unique=True)
    duration = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ManyToManyField(Course)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ManyToManyField(Course)
    date_posted = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='assignments')
    grade = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class LibraryBook(models.Model):
    title = models.CharField(max_length=255)
    course = models.ManyToManyField(Course)
    author = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=13, unique=True)
    available = models.BooleanField(default=True)




    def __str__(self):
        return self.title
