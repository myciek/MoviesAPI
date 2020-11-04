from rest_framework.routers import DefaultRouter
from django.urls import path, include
from comments.views import CommentsViewSet, TopAPIView

router = DefaultRouter()
app_name = 'comments'
router.register("", CommentsViewSet)

urlpatterns = [
    path("comments/", include(router.urls)),
    path("top/", TopAPIView.as_view(), name="top_comments"),
]
