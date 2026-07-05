from django.test import TestCase

from .models import Director, Movie


class CatalogModelTests(TestCase):
    def test_director_and_movies_relationship(self):
        director = Director.objects.create(name='Greta Gerwig', nationality='American', birth_year=1983)
        Movie.objects.create(title='Barbie', genre='Comedy', release_year=2023, streaming_service='Max', director=director)
        Movie.objects.create(title='Lady Bird', genre='Drama', release_year=2017, streaming_service='Netflix', director=director)

        self.assertEqual(director.movies.count(), 2)
