from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# دالة التحقق من أن المستخدم هو Librarian
def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
