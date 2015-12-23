from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
	url(r'^movies/', views.movies, name='movies'),
	url(r'^books/', views.books, name='books'),
]

urlpatterns += staticfiles_urlpatterns()
