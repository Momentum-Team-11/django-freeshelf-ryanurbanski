from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    description = models.CharField(max_length=2000)
    date = models.DateTimeField(auto_now_add=datetime.now)