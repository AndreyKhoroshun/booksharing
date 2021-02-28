from books.models import Book
from books.models import Author
from django.shortcuts import render
from books.forms import BookForm, AuthorForm
from django.http import HttpResponseRedirect


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


def book_create(request):
    form_data = request.POST
    if request.method == 'POST':
        form = BookForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books/list/')
    elif request.method == 'GET':
        form = BookForm()
    context = {'message': 'Create book',
               'form': form,
               }
    return render(request, 'books_create.html', context=context)


def author_create(request):
    form_data = request.POST
    if request.method == 'POST':
        form = AuthorForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/authors/list/')
    elif request.method == 'GET':
        form = AuthorForm()
    context = {'message': 'Create author',
               'form': form,
               }
    return render(request, 'authors_create.html', context=context)
