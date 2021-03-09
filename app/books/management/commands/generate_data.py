from django.core.management.base import BaseCommand
from books.models import Book, Author
from faker import Faker
import random
from datetime import datetime


class Command(BaseCommand):
    help = 'Generate Random Book' # noqa

    def handle(self, *args, **options):
        fake = Faker()
        books_list = []
        for _ in range(1000):
            author = fake.name()
            title = fake.word()
            publish_year = random.randint(0, datetime.now().year)
            review = fake.text()
            condition = random.randint(1, 5)
            books_list.append(Book(
                author=author,
                title=title,
                publish_year=publish_year,
                review=review,
                condition=condition,
            ))
        Book.objects.bulk_create(books_list)

        authors_list = []
        for _ in range(1000):
            name = fake.name()
            first_name = name.split()[0]
            last_name = name.split()[1]
            date_of_birth = fake.date()
            date_of_death = fake.date()
            country = fake.country()
            gender = random.choice(['male', 'female'])
            native_language = random.choice(['English', 'French', 'Russian', 'Ukrainian'])
            authors_list.append(Author(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                date_of_death=date_of_death,
                country=country,
                gender=gender,
                native_language=native_language,
            ))
        Author.objects.bulk_create(authors_list)
