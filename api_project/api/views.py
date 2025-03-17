from rest_framework import generics, viewsets, filters as drf_filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from .models import Book
from .serializers import BookSerializer


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains') 
    author = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains') 
    publication_year = django_filters.NumberFilter() 

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,  
        drf_filters.SearchFilter,     
        drf_filters.OrderingFilter    
    ]
    filterset_class = BookFilter
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
