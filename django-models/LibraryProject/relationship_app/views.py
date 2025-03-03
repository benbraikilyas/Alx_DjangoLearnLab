from django.views.generic.detail import DetailView
from .models import Library  # ✅ تأكد من استيراد Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # ✅ تأكد من وجود القالب بهذا الاسم
    context_object_name = "library"
