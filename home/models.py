from django.db import models

# Create your models here.

class Review(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'review_image', blank = True, null = True)
    review = models.TextField(max_length=500)
    rate = models.IntegerField(default=1)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name