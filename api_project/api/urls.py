from django.urls import path
from .views import BookList  # تأكد من استيراد الـ View الصحيحة

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
