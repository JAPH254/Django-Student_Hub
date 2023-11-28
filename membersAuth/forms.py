from django import forms
from app.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

# class Userregister( forms.ModelForm ):
#     class Meta:
#         model = Account
#         fields = ['name', 'email', 'phone',  'username', 'password']
        
class CreateUserForm(UserCreationForm):
    # phone = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email' ,'password1', 'password2']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class AddToCartForm(forms.Form):
    book_id = forms.IntegerField(widget=forms.HiddenInput())


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = registeredmails
        fields = ['email']