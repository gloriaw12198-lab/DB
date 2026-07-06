from django.shortcuts import render

from .models import Author, Book


def index(request):
    authors = Author.objects.all().order_by('name')
    books = Book.objects.select_related('author').prefetch_related('adapted_movies').all().order_by('title')
    return render(request, 'library/index.html', {'authors': authors, 'books': books})
