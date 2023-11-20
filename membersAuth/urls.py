# accounts/urls.py

from django.urls import path
from .views import register, sign_in, sign_out

urlpatterns = [
    path('register/', register, name='register'),
    path('sign-in/', sign_in, name='sign_in'),
    path('sign-out/', sign_out, name='sign_out'),
]
