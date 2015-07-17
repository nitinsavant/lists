from django.db import models

# Create your models here.
class Movie(models.Model):
	title = models.CharField(max_length=100)
	release_date = models.DateField(null=True, blank=True)
	watch_date = models.DateField(default='1900-01-01')
	imdb_link = models.URLField(null=True, blank=True)

	def __str__(self):
		return self.title
