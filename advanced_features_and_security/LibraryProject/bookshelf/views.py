from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import ExampleForm

def add_book(request):
    if request.method == "POST":
        book_title = request.POST.get("book_title", "").strip()
        if book_title:
            Book.objects.create(title=book_title)
            return HttpResponse("Book added successfully!")
    
    return render(request, "bookshelf/form_example.html")

from django.shortcuts import render
from .models import Book

def search_books(request):
    search_query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=search_query)  # استخدم Django ORM لتجنب SQL Injection
    return render(request, 'bookshelf/book_list.html', {'books': books})
