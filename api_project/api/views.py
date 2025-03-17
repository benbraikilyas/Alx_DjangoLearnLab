from rest_framework import generics
from .models import book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from django_filters import rest_framework 
from rest_framework import viewsets, filters as drf_filters


class BookList(generics.ListAPIView):
    queryset = book.objects.all()  
    serializer_class = BookSerializer

# إنشاء ViewSet للتعامل مع عمليات CRUD
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  
    serializer_class = BookSerializer  
    permission_classes = [IsAuthenticated] 

class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains') 
    author = filters.CharFilter(field_name='author__name', lookup_expr='icontains') 
    publication_year = filters.NumberFilter() 

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [
        filters.DjangoFilterBackend,  
        drf_filters.SearchFilter,     
        drf_filters.OrderingFilter    
    ]
    filterset_class = BookFilter


class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains') 
    author = filters.CharFilter(field_name='author__name', lookup_expr='icontains') 
    publication_year = filters.NumberFilter() 

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [
        filters.DjangoFilterBackend,  
        drf_filters.SearchFilter,     
        drf_filters.OrderingFilter    
    ]
    filterset_class = BookFilter
