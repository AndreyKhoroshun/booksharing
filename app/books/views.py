from books.models import Book
from books.models import Author
from books.models import Log
from django.shortcuts import render, get_object_or_404, redirect
from books.forms import BookForm, AuthorForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy


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


class BookCreate(CreateView):
    model = Book
    success_url = reverse_lazy('books-list')
    fields = (
        'author',
        'title',
        'publish_year',
        'review',
        'condition',
    )


class AuthorCreate(CreateView):
    model = Author
    success_url = reverse_lazy('authors-list')
    fields = (
        'first_name',
        'last_name',
        'date_of_birth',
        'date_of_death',
        'country',
        'gender',
        'native_language',
    )


class BookUpdate(UpdateView):
    model = Book
    success_url = reverse_lazy('books-list')
    fields = (
        'author',
        'title',
        'publish_year',
        'review',
        'condition',
    )


def book_update(request, pk):
    instance = get_object_or_404(Book, pk=pk)
    form_data = request.POST
    if request.method == 'POST':
        form = BookForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('books-list')
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
            return redirect('authors-list')
    elif request.method == 'GET':
        form = AuthorForm(instance=instance)
    context = {'message': 'Author update',
               'form': form,
               }
    return render(request, 'authors_create.html', context=context)


def book_delete(request, pk):
    instance = get_object_or_404(Book, pk=pk)
    instance.delete()
    return redirect('books-list')


def author_delete(request, pk):
    instance = get_object_or_404(Author, pk=pk)
    instance.delete()
    return redirect('authors-list')


def logs_list(request):
    context = {
        'logs_list': Log.objects.all()
    }
    return render(request, 'logs_list.html', context=context)
