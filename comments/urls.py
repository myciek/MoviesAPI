from django.urls import path, include

from comments.views import TopAPIView,CommentsListCreateAPIView

app_name = 'comments'


urlpatterns = [
    path("comments/", CommentsListCreateAPIView.as_view(), name="comments"),
    path("top/", TopAPIView.as_view(), name="top_comments"),
]
