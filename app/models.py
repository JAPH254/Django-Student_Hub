from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    phone = models.CharField(max_length=100, blank=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE ,null=True)
    year = models.CharField(max_length=100, blank=True)
    profile_pic = models.ImageField(default='client1.jpg', upload_to='users/',null=True, blank=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.user.username

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
    description = models.TextField( blank=True, default='write your description here...')
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
    
class Collection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(LibraryBook, related_name='collections')

    def __str__(self):
        return f"{self.user.username}'s Collection"
