from django.urls import path
from .views import list_books, LibraryDetailView  # تأكد من استيراد العروض (views)

urlpatterns = [
    path('books/', list_books, name='list_books'),  # العرض القائم على الدالة (Function-Based View)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # العرض القائم على الفئة (Class-Based View)
]
