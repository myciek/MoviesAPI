import django_filters

from movies.models import Movie

# Filter for Movie model
class MovieFilter(django_filters.FilterSet):

    class Meta:
        model = Movie
        fields = ["rated", "type"]