from django import forms
 
# creating a form
from .models import Book

class Bookentry(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets={
            'is_scifi':forms.CheckboxInput(),
            'is_drama':forms.CheckboxInput(),
            'is_novel':forms.CheckboxInput(),
            
        }