from books.models import Book
from books.models import Author
from django.shortcuts import render


def book_list(request):
    context = {
        'books_list': Book.objects.all(),
    }
    return render(request, 'books_list.html', context=context)


def author_list(request):
    context = {
        'author_list': Author.objects.all(),
    }
    return render(request, 'author_list.html', context=context)
