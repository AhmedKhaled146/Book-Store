from django.shortcuts import render
from .models import Review
# from ..books.models import Book
# Create your views here.

def index(request):
    
    context = {
        'review' : Review.objects.all(),
    }
    
    return render(request, 'home/index.html', context) 