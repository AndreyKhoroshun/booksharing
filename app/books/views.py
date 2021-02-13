from django.http import HttpResponse
from books.models import Book


def book_list(request):
    response_content = ''
    for book in Book.objects.all():
        response_content += f'ID: {book.id}, Author: {book.author} <br/>'
    return HttpResponse(response_content)
