from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")
        self.book1 = Book.objects.create(title="Django Basics", author="John Doe", publication_year=2020)
        self.book2 = Book.objects.create(title="Advanced Django", author="Jane Doe", publication_year=2021)
        self.book3 = Book.objects.create(title="Django REST Framework", author="John Doe", publication_year=2022)

    def test_get_book_list(self):     
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_create_book(self): 
        data = {"title": "New Book", "author": "Test Author", "publication_year": 2023}
        response = self.client.post("/api/books/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_update_book(self):
        update_data = {"title": "Updated Django Book", "author": "Updated Author", "publication_year": 2025}
        response = self.client.put(f"/api/books/{self.book1.id}/", update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django Book")

    def test_delete_book(self):
        response = self.client.delete(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    def test_filter_books_by_author(self):
        response = self.client.get("/api/books/?author=John Doe")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) 

    def test_search_books_by_title(self):
        response = self.client.get("/api/books/?search=Django Basics")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Django Basics")

    def test_order_books_by_year(self):
        response = self.client.get("/api/books/?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))  
