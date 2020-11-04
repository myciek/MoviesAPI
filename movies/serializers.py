from rest_framework import serializers

from movies.models import Movie, Rating


class CreateMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title",)


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("source", "value")


class MovieSerializer(serializers.ModelSerializer):
    raitings = RatingSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'
