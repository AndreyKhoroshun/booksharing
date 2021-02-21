from django.http import HttpResponse
from books.models import Book
from books.models import Author


def book_list(request):
    response_content = ''
    for book in Book.objects.all():
        response_content += f'ID: {book.id}, Author: {book.author} <br/>'
    return HttpResponse(response_content)


def author_list(request):
    response_content = ''
    for author in Author.objects.all():
        response_content += f'ID: {author.id}, Author: {author.last_name} <br/>'
    return HttpResponse(response_content)
