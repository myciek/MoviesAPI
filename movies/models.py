from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.TextField(max_length=255)
    year = models.TextField(max_length=4)
    rated = models.TextField(max_length=5)
    released = models.TextField(max_length=17)
    runtime = models.TextField(max_length=8)
    genre = models.TextField(max_length=255)
    director = models.TextField(max_length=255)
    writer = models.TextField(max_length=255)
    actors = models.TextField(max_length=255)
    plot = models.TextField(max_length=511)
    language = models.TextField(max_length=255)
    country = models.TextField(max_length=255)
    awards = models.TextField(max_length=255)
    poster = models.TextField(max_length=511)
    metascore = models.TextField(max_length=3)
    imdbRating = models.TextField(max_length=3)
    imdbVotes = models.TextField(max_length=12)
    imdbID = models.TextField(max_length=255)
    type = models.TextField(max_length=255)
    DVD = models.TextField(max_length=255)
    boxOffice = models.TextField(max_length=255)
    production = models.TextField(max_length=12)
    website = models.TextField(max_length=255)


class Rating(models.Model):
    source = models.TextField(max_length=255)
    value = models.TextField(max_length=255)

    movie = models.ForeignKey(Movie, related_name="ratings", on_delete=models.CASCADE)
