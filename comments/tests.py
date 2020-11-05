from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import date


# Create your tests here.


class CommentsTest(APITestCase):

    def setUp(self):
        self.movie = self.client.post(reverse("movies:movie-view-set-list"), {"title": "star wars"})

    def test_create_comment_wrong_parameters(self):
        res = self.client.post(reverse("comments:comments"))
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data, {
            "text": [
                "This field is required."
            ],
            "movie": [
                "This field is required."
            ]
        })

    def test_create_comment_wrong_id(self):
        res = self.client.post(reverse("comments:comments"), {"text": "123", "movie": 454354})
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data, {"movie": ["Invalid pk \"454354\" - object does not exist."]})

    def test_create_comment_success(self):
        res = self.client.post(reverse("comments:comments"), {"text": "123", "movie": self.movie.data["id"]})
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data["movie"], self.movie.data["id"])


class TopCommentsTest(APITestCase):
    def setUp(self):
        self.movie1 = self.client.post(reverse("movies:movie-view-set-list"), {"title": "star wars"})
        self.movie2 = self.client.post(reverse("movies:movie-view-set-list"), {"title": "titanic"})
        self.movie3 = self.client.post(reverse("movies:movie-view-set-list"), {"title": "indiana jones"})

        self.comment1 = self.client.post(reverse("comments:comments"), {"text": "123", "movie": self.movie2.data["id"]})
        self.comment2 = self.client.post(reverse("comments:comments"), {"text": "123", "movie": self.movie3.data["id"]})

    def test_top_comments_get_wrong_parameters(self):
        res = self.client.get(reverse("comments:top_comments"))
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data, "You have to specify date range!")

    def test_top_comments_get_success(self):
        res = self.client.get(reverse("comments:top_comments")+"?start=2020-01-01&end=2020-12-12")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data[2]["movie_id"], self.movie1.data["id"])
        self.assertEqual(res.data[0]["rank"], res.data[1]["rank"])
