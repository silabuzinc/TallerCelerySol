from django.shortcuts import render, redirect

from django.views.generic.list import ListView
from .models import Book
# Create your views here.

class BookList(ListView):
    model = Book
    template_name = "booklist.html"



def select_book(request, id):
    book = Book.objects.filter(bookID = id)
    request.session["authors"] = book[0].authors
    context = {}
    context["book"] = book[0]
    return render(request, "oneBook.html", context)


def author(request, id):
    context = {}
    context["author"] = request.session["authors"]
    return render(request, "author.html", context)

