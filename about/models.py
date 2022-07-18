from inspect import classify_class_attrs
from django.db import models

# Create your models here.

class About(models.Model):
    mission = models.TextField(max_length=5000)
    vision = models.TextField(max_length=50000)
    story = models.TextField(max_length=50000)
    work = models.TextField(max_length=5000)
    
