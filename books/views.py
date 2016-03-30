from django.views.generic import ListView
from two_factor.views import OTPRequiredMixin

from .models import Author, Book


class BookList(OTPRequiredMixin, ListView):
    model = Book


class AuthorList(ListView):
    model = Author
