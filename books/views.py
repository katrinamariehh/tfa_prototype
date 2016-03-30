from django.views.generic import ListView
from .models import Author, Book


class BookList(ListView):
    model = Book


class AuthorList(ListView):
    model = Author
