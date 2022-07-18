from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator
from .filter import BookFilter
# Create your views here.

def books(request): 
    Books = Book.objects.all()
    
    # filter
    myfilter = BookFilter(request.GET,queryset=Books)
    Books = myfilter.qs
   
    paginator = Paginator(Books, 9)
    page_num = request.GET.get('page')  
    Books_obj = paginator.get_page(page_num)
    
   
    context_books = {
        'count': paginator.count,
        'title': 'Books',
        'Books': Books_obj,
        'myfilter': myfilter, 
    }
    
    return render (request, 'books/books.html', context_books)

def book_info(request, slug):
    context = {
        'book_info': Book.objects.get(slug=slug),
    }
    return render (request, 'books/book_info.html', context)