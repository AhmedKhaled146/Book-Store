from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('',views.books, name="books"),
    path('<str:slug>', views.book_info, name='book_info')
]
