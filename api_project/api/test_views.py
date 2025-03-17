from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Author, Book
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User




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



class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test data
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter",
            publication_year=1997,
            author=self.author
        )
        # Create a test user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()

    # --- CRUD Tests ---
    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_single_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Harry Potter")

    def test_create_book_authenticated(self):
        self.client.force_authenticate(user=self.user)  # Authenticate the user
        url = reverse('book-list')
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        url = reverse('book-list')
        data = {"title": "Unauthorized Book", "publication_year": 2023}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --- Filtering, Searching, Ordering Tests ---
    def test_filter_by_publication_year(self):
        url = reverse('book-list') + '?publication_year=1997'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['publication_year'], 1997)

    def test_search_by_title(self):
        url = reverse('book-list') + '?search=Harry'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("Harry Potter" in [book['title'] for book in response.data])

    def test_order_by_title(self):
        Book.objects.create(title="A Book", publication_year=2000, author=self.author)
        url = reverse('book-list') + '?ordering=title'
        response = self.client.get(url)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, ["A Book", "Harry Potter"])

    # --- Validation Tests ---
    def test_invalid_publication_year(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('book-list')
        data = {"title": "Invalid Year", "publication_year": 3000, "author": self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
