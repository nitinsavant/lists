from django.shortcuts import render, get_object_or_404
import datetime
from .models import Book

def index(request):
	book_list_title = Book.objects.order_by('title')
	book_list_watch = Book.objects.order_by('-watch_date', '-release_date')
	book_list_release = Book.objects.order_by('-release_date')
	num_books = Book.objects.count()
	context = {'book_list_title': book_list_title,
				'book_list_watch': book_list_watch,
				'book_list_release': book_list_release,
				'num_books': num_books,
				}
	return render(request, 'books/index.html', context)
