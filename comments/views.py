from django.shortcuts import render

# Create your views here.
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from comments.models import Comment
from comments.serializers import CommentSerializer
from movies.models import Movie


class CommentsViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class TopAPIView(APIView):
    def get(self, request):
        if not request.data.get("start", None) or not request.data.get("end", None):
            return Response("You have to specify date range!", status=status.HTTP_400_BAD_REQUEST)
        movies = Movie.objects.all()
        comments_count = {movie.pk: len(movie.comments.filter(
            created__gte=request.data["start"]
        ).filter(
            created__lte=request.data["end"]
        ).all()) for movie in movies}
        sorted_count = {k: v for k, v in sorted(comments_count.items(), key=lambda item: item[1], reverse=True)}

        rank = 1
        previous_count = 0
        ranking = []
        for movie_id, count in sorted_count.items():
            if count < previous_count:
                rank += 1

            ranking.append(
                {
                    "movie_id": movie_id,
                    "total_comments": count,
                    "rank": rank
                }
            )
            previous_count = count
        return Response(ranking)
