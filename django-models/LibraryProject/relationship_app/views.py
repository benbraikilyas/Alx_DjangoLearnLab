from django.shortcuts import render
from .models import Book

# عرض وظيفي لعرض جميع الكتب
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})



from django.views.generic import DetailView
from .models import Library

# عرض كائني لعرض تفاصيل مكتبة معينة
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # ربط العرض بالقالب المناسب
    context_object_name = 'library'  # تغيير اسم المتغير داخل القالب


from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # مسار القالب الصحيح
    context_object_name = 'library'  # الاسم المستخدم في القالب
