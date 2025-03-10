from django.urls import path
from .views import BookList  # تأكد من استيراد الـ View الصحيحة
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView) - if you still want to keep it separately
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for the BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]
