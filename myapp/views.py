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
    request.session["id"] = book[0].bookID
    context = {}
    context["book"] = book[0]
    return render(request, "oneBook.html", context)


def author(request, id):
    context = {}
    context["author"] = request.session["authors"]
    context["id"] = request.session["id"]
    if id != context["id"]:
        book = Book.objects.filter(bookID = id)
        if not book:
            context["author"] = "No existe el autor"
        else:
            context["author"] = book[0].authors
    return render(request, "author.html", context)

class BookListView(ListView):
        model = Book
        template_name = 'booklist.html'
        queryset = Book.objects.order_by("bookID")[:10]

