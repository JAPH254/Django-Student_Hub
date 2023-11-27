
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
    path('add-to-collection/<int:book_id>/', add_to_collection, name='add_to_collection'),
    path('collection/', CollectionListView.as_view(), name='collection'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),

]

