
from django.urls import path
from .views import *
from app.views import *
from membersAuth.views import *
urlpatterns = [
    path('filterbytitle/', filterbytitle, name='filterbytitle'),
    path('filterbyauthor/', filterbyauthor, name='filterbyauthor'),
    path('filterbyISBN/', filterbyISBN, name='filterbyISBN'),
    path('assignments/', assignments, name='assignments'),
    path('notifications/', notifications, name='notifications'),
    path('profile/', profile, name='profile'),
    path('library/', library, name='library'),
    path('about/', about, name='about'),
    path('search/', searchBar, name='search'),
    path('update-profile/', update_profile, name='update_profile'),
    path('infopage/', infopage, name='infopage'),
    path('books/', book_list, name='book_list'),
    # path('add_to_collection/<int:book_id>/', add_to_collection, name='add_to_collection'),
    path('collection/', collection, name='collection'),
    path('managesubscribers/', managesubscribers, name='managesubscribers'),
    path('move_user/<int:book_id>/', move_user, name='move_user'),
    path('request_book/<int:book_id>/', request_book, name='request_book'),
    path('chat/<str:username>/', chat, name='chat'),
]

