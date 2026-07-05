from django.core.management.base import BaseCommand
from library.models import Author, Book


class Command(BaseCommand):
    help = 'Seed the database with sample authors and books'

    def handle(self, *args, **options):
        Book.objects.all().delete()
        Author.objects.all().delete()

        author1 = Author.objects.create(name='Jane Austen', nationality='British')
        author2 = Author.objects.create(name='George Orwell', nationality='British')

        Book.objects.create(title='Pride and Prejudice', author=author1, genre='Classic', publication_year=1813)
        Book.objects.create(title='1984', author=author2, genre='Dystopian', publication_year=1949)
        Book.objects.create(title='Animal Farm', author=author2, genre='Satire', publication_year=1945)

        self.stdout.write(self.style.SUCCESS('Seeded library data'))
