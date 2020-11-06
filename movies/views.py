from django.shortcuts import render

# Create your views here.
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from movies.filters import MovieFilter
from movies.models import Movie
from movies.serializers import MovieSerializer, CreateMovieSerializer, RatingSerializer
from movies.utils import get_movie_from_api
from rest_framework.filters import OrderingFilter

# ViewSet for movie model
# [GET] - list of all movies
# Optional parameters:
# filtering: /movies?<filter>=<data> where <filter> can be rated or type
# sorting: /movies?ordering=year from oldest or /movies?ordering=-year from newest
# [POST] with {"title": movie_title} - retrieves data from http://www.omdbapi.com , creates movie object and returns movie data
# [PATCH] /id - with body with fields you want to change
# [DELETE] /id - if movie exists delete it
class MoviesViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = MovieFilter
    ordering_fields = ("year",)

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
                movie.ratings.add(rating.pk)

        movie.save()
        movie_serializer = self.serializer_class(movie)

        return Response(movie_serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        try:
            movie = Movie.objects.get(pk=kwargs["pk"])
            for rating in movie.ratings.all():
                rating.delete()
            movie.delete()
            return Response("Movie deleted", status=status.HTTP_200_OK)
        except Movie.DoesNotExist:
            return Response("Movie with this id not found", status=status.HTTP_404_NOT_FOUND)
