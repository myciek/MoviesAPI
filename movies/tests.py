# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CreateMovieTest(APITestCase):

    def setUp(self):
        self.movie_example = {
            "title": "Star Wars: Episode IV - A New Hope",
            "ratings": [
                {
                    "source": "Internet Movie Database",
                    "value": "8.6/10"
                },
                {
                    "source": "Rotten Tomatoes",
                    "value": "92%"
                },
                {
                    "source": "Metacritic",
                    "value": "90/100"
                }
            ],
        }

    def test_create_movie_wrong_parameters(self):
        res = self.client.post(reverse("movies:movie-view-set-list"))
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_movie_title_not_found(self):
        res = self.client.post(reverse("movies:movie-view-set-list"), {"title": "definitely not a movie title"})
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data, "Movie with this title not found")

    def test_create_movie_success(self):
        res = self.client.post(reverse("movies:movie-view-set-list"), {"title": "star wars"})
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data["title"], self.movie_example["title"])
        self.assertEqual(res.data["ratings"], self.movie_example["ratings"])


class GetMoviesTest(APITestCase):
    def setUp(self):
        self.series = self.client.post(reverse("movies:movie-view-set-list"), {"title": "game of thrones"})
        self.movie = self.client.post(reverse("movies:movie-view-set-list"), {"title": "star wars"})

    def test_get_movies(self):
        res = self.client.get(reverse("movies:movie-view-set-list"))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)

    def test_get_movies_filtering(self):
        res = self.client.get(reverse("movies:movie-view-set-list") + "?type=series")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]["title"], self.series.data["title"])

    def test_get_movies_ordering(self):
        res = self.client.get(reverse("movies:movie-view-set-list") + "?ordering=year")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data[0]["title"], self.movie.data["title"])


class UpdateMovieTest(APITestCase):
    def setUp(self):
        self.movie = self.client.post(reverse("movies:movie-view-set-list"), {"title": "star wars"})

    def test_update_movie_wrong_id(self):
        res = self.client.patch(reverse("movies:movie-view-set-detail", kwargs={"pk": 56333}))
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(res.data, {"detail": "Not found."})

    def test_update_movie_success(self):
        title = "not start wars"
        res = self.client.patch(
            reverse("movies:movie-view-set-detail", kwargs={"pk": self.movie.data["id"]}), {"title": title})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["title"], title)


class DeleteMovieTest(APITestCase):
    def setUp(self):
        self.movie = self.client.post(reverse("movies:movie-view-set-list"), {"title": "star wars"})

    def test_delete_movie_wrong_id(self):
        res = self.client.delete(reverse("movies:movie-view-set-detail", kwargs={"pk": 56333}))
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(res.data, "Movie with this id not found")

    def test_delete_movie_success(self):
        res = self.client.delete(
            reverse("movies:movie-view-set-detail", kwargs={"pk": self.movie.data["id"]}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, "Movie deleted")

        res = self.client.get(
            reverse("movies:movie-view-set-detail", kwargs={"pk": self.movie.data["id"]}))
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
