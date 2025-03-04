from django.shortcuts import render
from .models import Book  # ✅ تأكد من استيراد Book
from django.views.generic.detail import DetailView  # ✅ تأكد من وجود هذا الاستيراد
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test

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





from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # استبدل 'home' بصفحتك الرئيسية
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# تحقق مما إذا كان المستخدم "Admin"
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


# تحقق مما إذا كان المستخدم "Librarian"
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# تحقق مما إذا كان المستخدم "Member"
def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


