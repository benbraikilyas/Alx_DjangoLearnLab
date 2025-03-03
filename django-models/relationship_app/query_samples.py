import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')


from relationship_app.models import Author, Book, Library, Librarian

# 1️⃣ استعلام جميع الكتب لمؤلف معين
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# 2️⃣ استعلام جميع الكتب في مكتبة معينة
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3️⃣ استعلام أمين المكتبة لمكتبة معينة
def get_librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian


