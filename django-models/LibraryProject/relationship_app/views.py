from django.shortcuts import render
from .models import Book  # ✅ تأكد من استيراد Book
from django.views.generic.detail import DetailView  # ✅ تأكد من وجود هذا الاستيراد
from .models import Library
from django.contrib.auth.forms import UserCreationForm


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

