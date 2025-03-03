from django.shortcuts import render
from .models import Book  # ✅ تأكد من استيراد Book
from django.views.generic.detail import DetailView  # ✅ تأكد من وجود هذا الاستيراد
from .models import Library

def list_books(request):
    books = Book.objects.all()  # ✅ تأكد من استخدام الاستعلام الصحيح
    return render(request, "relationship_app/list_books.html", {"books": books})  # ✅ تأكد من استخدام القالب الصحيح

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView  # ✅ تأكد من استيراد DetailView
from .models import Library  # ✅ تأكد من استيراد Library

class LibraryDetailView(DetailView):
    model = Library  # ✅ تعيين النموذج المرتبط
    template_name = "relationship_app/library_detail.html"  # ✅ التأكد من استخدام القالب الصحيح
    context_object_name = "library"  # ✅ التأكد من استخدام الاسم الصحيح في القالب





