from .models import Book
from django import forms

class InputForm(forms.Form):

    nombre = forms.CharField(max_length = 3)
    email = forms.EmailField()