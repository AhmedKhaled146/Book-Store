from datetime import datetime
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Book(models.Model):
    
    langauge = [
        ('Arabic', 'Arabic'),
        ('English', 'English'),
    ]
    
    type = [
        ('PDF', 'PDF'),
        ('WORD', 'WORD'),
        ('other', 'other')
    ]
    
    book_name = models.CharField(max_length=50)
    auther = models.CharField(max_length=40)
    rate = models.PositiveSmallIntegerField()
    book_image = models.ImageField(upload_to = 'Books_photo')
    active = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    lang_book = models.CharField(max_length=10, choices=langauge)
    book_type = models.CharField(max_length=10, choices=type)
    NO_Pages = models.IntegerField(default=200)
    description = models.TextField(max_length=50000)
    pdf_file = models.FileField()
    datetime_uploaded = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(allow_unicode=True,null=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.book_name, allow_unicode=True)
        super(Book, self).save(*args, **kwargs)
        
        
    def __str__(self):
        return self.book_name
    
    
class Category(models.Model):
    category_name = models.CharField(max_length=40)
    
    
    def __str__(self):
        return self.category_name
