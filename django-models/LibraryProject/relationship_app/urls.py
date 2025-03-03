from django.urls import path
from .views import list_books, LibraryDetailView  # تأكد من استيراد العروض (views)
from .views import login_view, logout_view, register_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # العرض القائم على الدالة (Function-Based View)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # العرض القائم على الفئة (Class-Based View)
]



from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # المسار للـ function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # المسار للـ class-based view
]



urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]



urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
