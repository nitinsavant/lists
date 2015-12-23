from django.contrib import admin

# Register your models here.
from .models import Movie, Book

admin.site.register(Movie)
admin.site.register(Book)
