from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # رابط لعرض الكتب
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # رابط لعرض مكتبة معينة
]
