from rest_framework.routers import DefaultRouter
from django.urls import path, include
from movies.views import MoviesViewSet

router = DefaultRouter()
app_name = 'movies'
router.register("", MoviesViewSet, basename="movie-view-set")

urlpatterns = [
    path("", include(router.urls)),
]
