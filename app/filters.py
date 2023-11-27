
import django_filters
from .models import *

class BookFilterbytitle(django_filters.FilterSet):
    class Meta:
        model = LibraryBook
        fields = ['title']
class BookFilterbyauthor(django_filters.FilterSet):
    class Meta:
        model = LibraryBook
        fields = ['author']
class BookFilterbyISBN(django_filters.FilterSet):
    class Meta:
        model = LibraryBook
        fields = ['ISBN']
