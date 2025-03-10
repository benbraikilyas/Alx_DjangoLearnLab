from rest_framework import generics
from .models import book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 

class BookList(generics.ListAPIView):
    queryset = book.objects.all()  
    serializer_class = BookSerializer

# إنشاء ViewSet للتعامل مع عمليات CRUD
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # جلب جميع الكتب من قاعدة البيانات
    serializer_class = BookSerializer  # استخدام BookSerializer لتحويل البيانات
    permission_classes = [IsAuthenticated]  # السماح فقط للمستخدمين المفعلين بالوصول
