from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Author, Book
class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.force_authenticate(user=self.user)  

        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(title="Harry Potter", publication_year=2001, author=self.author)

        self.book_url = "/api/books/"
        self.book_detail_url = f"/api/books/{self.book.id}/"

    def test_get_books_list(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Harry Potter", response.data[0]["title"])

    def test_create_book(self):
        new_book = {
            "title": "The Hobbit",
            "publication_year": 1937,
            "author": self.author.id
        }
        response = self.client.post(self.book_url, new_book, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)


    def test_get_book_detail(self):
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Harry Potter")

    def test_update_book(self):
        updated_data = {
            "title": "Harry Potter and the Chamber of Secrets",
            "publication_year": 2002,
            "author": self.author.id
        }
        response = self.client.put(self.book_detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Harry Potter and the Chamber of Secrets")

    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
