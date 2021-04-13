from django.db import models
from books import model_choices as mch


def book_upload_cover(instance, filename):
    path = f'covers/{instance.user_id}/{filename}'
    return path


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=20)
    date_of_death = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    native_language = models.CharField(max_length=20)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=128)


class Book(models.Model):
    title = models.CharField(max_length=128)
    publish_year = models.PositiveSmallIntegerField()
    review = models.CharField(max_length=512)
    condition = models.PositiveSmallIntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, default=None)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE,
                             null=True, default=None)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,
                               null=True, default=None)
    cover = models.FileField(null=True, default=None, upload_to=book_upload_cover)


class Log(models.Model):
    path = models.CharField(max_length=512)
    method = models.CharField(max_length=128)
    time = models.PositiveIntegerField()


class RequestBook(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    recipient = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(choices=mch.REQUEST_STATUSES)
