from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
admin.site.register(Account)
admin.site.register(Course)
admin.site.register(Announcement)
admin.site.register(Assignment)
admin.site.register(LibraryBook)


class Accountinline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'

class CustomizedUserAdmin(UserAdmin):
    inlines = (Accountinline, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)