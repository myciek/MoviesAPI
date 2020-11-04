from rest_framework.routers import DefaultRouter
from django.urls import path, include
from comments.views import CommentsViewSet

router = DefaultRouter()
app_name = 'comments'
router.register("", CommentsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
