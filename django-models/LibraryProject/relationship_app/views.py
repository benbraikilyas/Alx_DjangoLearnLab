from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView

# عرض وظيفي لعرض جميع الكتب
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # ربط العرض بالقالب المناسب
    context_object_name = 'library'  # تغيير اسم المتغير داخل القالب

