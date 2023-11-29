from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='images/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    

    def __str__(self):
        return self.username
    

class BookRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey('LibraryBook', on_delete=models.CASCADE) 
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title} Request"

class Course(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)
    code = models.CharField(max_length=100, blank=False, unique=True)
    duration = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name


class Message(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

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
    file = models.FileField(upload_to='documents/',default='This cannot be downloaded')




    def __str__(self):
        return self.title
    
class Collect(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    books = models.ManyToManyField(LibraryBook, related_name='collection')

    def __str__(self):
        return f"{self.user.username}'s Collection"

class registeredmails(models.Model):
    email = models.EmailField(max_length=100, blank=False, unique=True)

    def __str__(self):
        return self.email