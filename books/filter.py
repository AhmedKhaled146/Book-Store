import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    book_name = django_filters.CharFilter(lookup_expr='icontains')
    auther = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['datetime_uploaded', 'book_image', 'active', 'rate', 'book_type', 'NO_Pages', 'pdf_file', 'slug']