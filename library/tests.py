from django.test import TestCase
from django.urls import reverse

from .models import Author, Book


class LibraryModelTests(TestCase):
    def test_book_belongs_to_author(self):
        author = Author.objects.create(name='Test Author', nationality='Testland')
        book = Book.objects.create(title='Test Book', genre='Fiction', publication_year=2024, author=author)

        self.assertEqual(book.author, author)
        self.assertIn(book, author.books.all())

    def test_index_view_renders_books(self):
        author = Author.objects.create(name='Sample Author', nationality='Example')
        Book.objects.create(title='Sample Book', genre='Drama', publication_year=2025, author=author)

        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sample Book')
        self.assertContains(response, '2025')
