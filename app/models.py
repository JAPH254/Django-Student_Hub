from django.db import models
from django.conf import settings
from membersAuth.models import CustomUser

# Book request model linking users to library books
class BookRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey('LibraryBook', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title} Request"

# Course model
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Message model for sending messages between users
class Message(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender.username} to {self.receiver.username}"

# Announcement model linked to courses
class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ManyToManyField(Course)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Assignment model linked to courses with file upload
class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='write your description here...')
    course = models.ManyToManyField(Course)
    date_posted = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='assignments')
    grade = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

# Library book model linked to courses
class LibraryBook(models.Model):
    title = models.CharField(max_length=255)
    course = models.ManyToManyField(Course)
    author = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=13, unique=True)
    available = models.BooleanField(default=True)
    file = models.FileField(upload_to='documents/', default='This cannot be downloaded')

    def __str__(self):
        return self.title

# User's book collection model
class Collect(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    books = models.ManyToManyField(LibraryBook, related_name='collections')

    def __str__(self):
        return f"{self.user.username}'s Collection"

# Registered emails model
class Registeredmails(models.Model):
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.email
