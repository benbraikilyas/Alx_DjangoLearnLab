from django.shortcuts import render
from .models import Book

# عرض وظيفي لعرض جميع الكتب
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

