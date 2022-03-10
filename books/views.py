from typing import List
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin

# from .forms import NotesForm
from .models import Books

def home(request):
    if request.user.is_authenticated:
        return redirect("list_albums")
    return render(request, "books/home.html")


class BooksListView(ListView):
    model = Books
    context_object_name = "list_books"
    template_name = "books/books_list.html"
    # login_url = "/admin"

    # def get_queryset(self):
    #     return self.request.user.books.all()