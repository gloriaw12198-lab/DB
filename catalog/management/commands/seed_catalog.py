from django.core.management.base import BaseCommand

from catalog.models import Director, Movie
from library.models import Book


class Command(BaseCommand):
    help = 'Seed the catalog with recent movie releases'

    def handle(self, *args, **options):
        Movie.objects.all().delete()
        Director.objects.all().delete()

        directors_data = [
            {
                'name': 'Greta Gerwig',
                'nationality': 'American',
                'birth_year': 1983,
                'movies': [
                    {'title': 'Barbie', 'genre': 'Comedy', 'release_year': 2023, 'streaming_service': 'Max', 'book_title': 'Pride and Prejudice'},
                ],
            },
            {
                'name': 'Denis Villeneuve',
                'nationality': 'Canadian-French',
                'birth_year': 1967,
                'movies': [
                    {'title': 'Dune: Part Two', 'genre': 'Sci-Fi', 'release_year': 2024, 'streaming_service': 'Max', 'book_title': '1984'},
                ],
            },
            {
                'name': 'Ryan Coogler',
                'nationality': 'American',
                'birth_year': 1986,
                'movies': [
                    {'title': 'Sinners', 'genre': 'Horror', 'release_year': 2025, 'streaming_service': 'Hulu', 'book_title': 'Animal Farm'},
                ],
            },
            {
                'name': 'Kelsey Mann',
                'nationality': 'American',
                'birth_year': 1980,
                'movies': [
                    {'title': 'Inside Out 2', 'genre': 'Animation', 'release_year': 2024, 'streaming_service': 'Disney+', 'book_title': None},
                ],
            },
        ]

        for director_data in directors_data:
            director = Director.objects.create(
                name=director_data['name'],
                nationality=director_data['nationality'],
                birth_year=director_data['birth_year'],
            )
            for movie_data in director_data['movies']:
                book = None
                if movie_data.get('book_title'):
                    book = Book.objects.filter(title=movie_data['book_title']).first()
                Movie.objects.create(director=director, book=book, **{k: v for k, v in movie_data.items() if k != 'book_title'})

        self.stdout.write(self.style.SUCCESS('Seeded the latest catalog entries.'))
