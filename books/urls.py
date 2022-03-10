from django.urls import path

from . import views as book_views

urlpatterns = [
    path("", book_views.homepage, name="homepage"),
    path("books/", book_views.book_list, name="book_list"),
]