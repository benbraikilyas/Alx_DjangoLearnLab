from django.test import TestCase
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorSerializerTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(title="Harry Potter and the Philosopher's Stone", publication_year=1997, author=self.author)

    def test_author_serializer(self):
        serializer = AuthorSerializer(self.author)
        expected_data = {
            'id': self.author.id,
            'name': self.author.name,
            'books': [
                {
                    'id': self.book.id,
                    'title': self.book.title,
                    'publication_year': self.book.publication_year,
                }
            ]
        }
        self.assertEqual(serializer.data, expected_data)

class BookSerializerTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="George Orwell")
        self.book = Book.objects.create(title="1984", publication_year=1949, author=self.author)

    def test_book_serializer(self):
        serializer = BookSerializer(self.book)
        expected_data = {
            'id': self.book.id,
            'title': self.book.title,
            'publication_year': self.book.publication_year,
            'author': self.author.id
        }
        self.assertEqual(serializer.data, expected_data)

    def test_invalid_publication_year(self):
        invalid_book_data = {
            'title': "Invalid Book",
            'publication_year': 2025,  # Future year
            'author': self.author.id
        }
        serializer = BookSerializer(data=invalid_book_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('publication_year', serializer.errors)