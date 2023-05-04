import datetime
from django.db import models
from django.forms import forms

class Book(models.Model):
    name = models.CharField(max_length = 200)
    p_name = models.CharField(max_length = 200)
    age = models.IntegerField(max_length=2)
    date=models.DateField(default=datetime.date.today)
    page=models.IntegerField(default=0)
    is_scifi=models.BooleanField(default=False)
    is_drama=models.BooleanField(default=False)
    is_novel=models.BooleanField(default=False)
    

# Create your models here.

