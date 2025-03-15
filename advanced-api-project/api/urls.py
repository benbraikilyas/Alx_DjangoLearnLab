from django.urls import path
from .views import (
    bookListView,
    bookdetailView,
    bookCreateView,
    bookupdateView,
    bookDeleteView
)

urlpatterns = [
    path('books/', bookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', bookdetailView.as_view(), name='book-detail'),
    path('books/create/', bookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', bookupdateView.as_view(), name='book-update'), 
    path('books/<int:pk>/delete/', bookdeleteView.as_view(), name='book-delete'),  
    
]

