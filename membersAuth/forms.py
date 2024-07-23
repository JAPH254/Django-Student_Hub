from django import forms
from app.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class YourUserDetailsForm(forms.ModelForm):
    class Meta:
        model = User  
        fields = ['first_name', 'last_name','username','email']  


class AddToCartForm(forms.Form):
    book_id = forms.IntegerField(widget=forms.HiddenInput())


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Registeredmails
        fields = ['email']



class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    profile_picture = forms.ImageField(required=False)
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = CustomUser  # If using a custom user model
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_picture', 'phone_number', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'profile_picture', 'phone_number']

class BookRequestForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']