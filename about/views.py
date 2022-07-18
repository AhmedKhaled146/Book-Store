from django.shortcuts import render
from .models import About
# Create your views here.

def about(request):
    about = About.objects.get(id = 1)
    # about = About.objects.first()
    context = {
        'about': about,
        'title': 'About Us'
    }
    return render (request, 'about/about.html', context)