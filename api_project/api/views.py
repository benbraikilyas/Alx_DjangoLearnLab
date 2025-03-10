from rest_framework import generics
from .models import book
from .serializers import BookSerializer
from rest_framework import viewsets

class BookList(generics.ListAPIView):
    queryset = book.objects.all()  
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = book.objects.all()
    serializer_class = BookSerializer