from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

admin.site.register(Course)
admin.site.register(Announcement)
admin.site.register(Assignment)
admin.site.register(LibraryBook)
admin.site.register(CustomUser)
admin.site.register(Message)


