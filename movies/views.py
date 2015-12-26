from django.shortcuts import render, get_object_or_404
import datetime
from .models import Movie, Book

def movies(request):
	movie_list_title = Movie.objects.order_by('title')
	movie_list_watch = Movie.objects.order_by('-watch_date', '-release_date')
	movie_list_release = Movie.objects.order_by('-release_date')
	num_movies = Movie.objects.count()
	context = {'movie_list_title': movie_list_title,
				'movie_list_watch': movie_list_watch,
				'movie_list_release': movie_list_release,
				'num_movies': num_movies,
				}
	return render(request, 'movies/movies.html', context)
	# return HttpResponse("I've watched %s movies" % num_movies)


def books(request):
	book_list_title = Book.objects.order_by('title')
	book_list_watch = Book.objects.order_by('-watch_date', '-release_date')
	book_list_release = Book.objects.order_by('-release_date')
	book_list_author = Book.objects.order_by('author')
	num_books = Book.objects.count()
	context = {'book_list_title': book_list_title,
				'book_list_watch': book_list_watch,
				'book_list_release': book_list_release,
				'book_list_author': book_list_author,
				'num_books': num_books,
				}
	return render(request, 'movies/books.html', context)
