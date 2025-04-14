from django.test import TestCase
from django.urls import reverse
from .models import Movie

class MovieModelTests(TestCase):
    def setUp(self):
        Movie.objects.create(
            id=1,
            name="Test Movie",
            description="Test Description",
            imgPath="test.jpg",
            duration=120,
            genre=["Action", "Adventure"],
            language="English",
            mpaa_rating_type="PG",
            mpaa_rating_label="Some Violence",
            user_rating="4"
        )

    def test_movie_str(self):
        movie = Movie.objects.get(id=1)
        self.assertEqual(str(movie), "Test Movie")

class MovieViewTests(TestCase):
    def setUp(self):
        Movie.objects.create(
            id=1,
            name="Test Movie",
            description="Test Description",
            imgPath="test.jpg",
            duration=120,
            genre=["Action", "Adventure"],
            language="English",
            mpaa_rating_type="PG",
            mpaa_rating_label="Some Violence",
            user_rating="4"
        )

    def test_movie_list_view(self):
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Movie")

    def test_movie_detail_view(self):
        response = self.client.get(reverse('movie_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Movie")
        self.assertContains(response, "Test Description")
