from books.models import Book
from books.models import Author
from django.shortcuts import render, get_object_or_404
from books.forms import BookForm, AuthorForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, 'index.html')


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
            return HttpResponseRedirect(reverse('books-list'))
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
            return HttpResponseRedirect(reverse('authors-list'))
    elif request.method == 'GET':
        form = AuthorForm()
    context = {'message': 'Create author',
               'form': form,
               }
    return render(request, 'authors_create.html', context=context)


def book_update(request, pk):
    instance = get_object_or_404(Book, pk=pk)
    form_data = request.POST
    if request.method == 'POST':
        form = BookForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('books-list'))
    elif request.method == 'GET':
        form = BookForm(instance=instance)
    context = {'message': 'Book update',
               'form': form,
               }
    return render(request, 'books_create.html', context=context)


def author_update(request, pk):
    instance = get_object_or_404(Author, pk=pk)
    form_data = request.POST
    if request.method == 'POST':
        form = AuthorForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authors-list'))
    elif request.method == 'GET':
        form = AuthorForm(instance=instance)
    context = {'message': 'Author update',
               'form': form,
               }
    return render(request, 'authors_create.html', context=context)


def book_delete(request, pk):
    instance = get_object_or_404(Book, pk=pk)
    instance.delete()
    return HttpResponseRedirect(reverse('books-list'))


def author_delete(request, pk):
    instance = get_object_or_404(Author, pk=pk)
    instance.delete()
    return HttpResponseRedirect(reverse('authors-list'))
