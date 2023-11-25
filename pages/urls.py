
from django.urls import path
from .views import *
urlpatterns = [
    path('library/', library, name='library'),
    path('assignments/', assignments, name='assignments'),
    path('notifications/', notifications, name='notifications'),
    path('profile/', profile, name='profile'),
    path('about/', about, name='about'),
]

from django.urls import path
from .views import *
urlpatterns = [
    path('library/', library, name='library'),
    path('assignments/', assignments, name='assignments'),
    path('notifications/', notifications, name='notifications'),
    path('profile/', profile, name='profile'),
    path('about/', about, name='about'),
]

