from django.db import models

# Create your models here.
from movies.models import Movie


class Comment(models.Model):
    text = models.TextField(max_length=511)
    movie = models.ForeignKey(Movie, related_name="comments", on_delete=models.CASCADE)