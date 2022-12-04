from django.urls import path
from myapp import views
from django.views.decorators.cache import cache_page
urlpatterns = [
    path("", cache_page(60*15)(views.BookList.as_view()), name="BookList"),
    path("book/<id>", views.select_book, name = "OneBook"),
    path("book/<id>/author", views.author, name="onlyAuthor")
]