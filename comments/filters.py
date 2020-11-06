import django_filters

from comments.models import Comment

# Filter for Comment model
# fields : movie
class CommentFilter(django_filters.FilterSet):

    class Meta:
        model = Comment
        fields = ["movie"]