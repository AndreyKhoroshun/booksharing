from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    publish_year = models.PositiveSmallIntegerField()
    review = models.CharField(max_length=512)
    condition = models.PositiveSmallIntegerField()


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=20)
    date_of_death = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    native_language = models.CharField(max_length=20)
