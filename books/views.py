from django.shortcuts import render


from http.client import CREATED
from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Book
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.views import LoginView



def homepage(request):
    if request.user.is_authenticated:
        return redirect("book_list")
    return render(request, "home.html")   
    
@login_required    
def book_list(request):
    books = Book.objects.all().order_by("date")
    return render(request, "book_list.html", {"books": books})

    