from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from movies.models import Movie
from movies.serializers import MovieSerializer, CreateMovieSerializer, RatingSerializer
from movies.utils import get_movie_from_api


class MoviesViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def create(self, request):
        create_movie_serializer = CreateMovieSerializer(data=request.data)
        create_movie_serializer.is_valid(raise_exception=True)
        try:
            movie_data = get_movie_from_api(create_movie_serializer.validated_data["title"])
        except LookupError as error:
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
        try:
            movie = Movie.objects.get(title=movie_data["title"])
        except Movie.DoesNotExist:
            ratings = movie_data.pop("ratings")
            movie = Movie(**movie_data)
            movie.save()

            for rating in ratings:
                rating = {key.lower(): value for key, value in rating.items()}
                rating_serializer = RatingSerializer(data=rating)
                rating_serializer.is_valid(raise_exception=True)
                rating = rating_serializer.save()
                movie.raitings.add(rating.pk)

        movie.save()
        movie_serializer = self.serializer_class(movie)

        return Response(movie_serializer.data, status=status.HTTP_201_CREATED)
