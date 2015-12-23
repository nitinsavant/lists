from django.shortcuts import render, get_object_or_404
import datetime
from .models import Movie

def index(request):
	movie_list_title = Movie.objects.order_by('title')
	movie_list_watch = Movie.objects.order_by('-watch_date', '-release_date')
	movie_list_release = Movie.objects.order_by('-release_date')
	num_movies = Movie.objects.count()
	context = {'movie_list_title': movie_list_title,
				'movie_list_watch': movie_list_watch,
				'movie_list_release': movie_list_release,
				'num_movies': num_movies,
				}
	return render(request, 'movies/index.html', context)
	# return HttpResponse("I've watched %s movies" % num_movies)
