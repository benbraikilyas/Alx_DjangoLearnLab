from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def add_book(request):
    if request.method == "POST":
        book_title = request.POST.get("book_title", "").strip()
        if book_title:
            Book.objects.create(title=book_title)
            return HttpResponse("Book added successfully!")
    
    return render(request, "bookshelf/form_example.html")

