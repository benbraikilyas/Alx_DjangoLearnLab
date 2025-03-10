from . import views
from django.urls import path
from .views import list_books, LibraryDetailView  # تأكد من استيراد العروض (views)
from .views import login_view, logout_view, register_view
from django.contrib.auth.views import LoginView, LogoutView
from .views import add_book, edit_book, delete_book
from .views.admin_view import admin_view



urlpatterns = [
    path('books/', list_books, name='list_books'),  # العرض القائم على الدالة (Function-Based View)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # العرض القائم على الفئة (Class-Based View)
]

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]

urlpatterns = [
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
]


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]



urlpatterns = [
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]

urlpatterns = [
    path('admin-view/', admin_view, name='admin_view'),
]

from django.urls import path
from .views import add_book, edit_book  # تأكد من استيراد الدوال الصحيحة

urlpatterns = [
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),  # إذا كان يحتاج إلى معرف
]



from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # تأكد من تضمين التطبيق الفرعي
]

