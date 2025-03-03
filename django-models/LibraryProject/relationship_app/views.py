from django.shortcuts import render
from .models import Book  # ✅ تأكد من استيراد Book

def list_books(request):
    books = Book.objects.all()  # ✅ تأكد من استخدام الاستعلام الصحيح
    return render(request, "relationship_app/list_books.html", {"books": books})  # ✅ تأكد من استخدام القالب الصحيح
