from rest_framework import generics
from .models import book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = book.objects.all()  
    serializer_class = BookSerializer