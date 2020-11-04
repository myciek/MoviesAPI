from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentsViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()