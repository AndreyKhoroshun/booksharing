from books.models import Book
from books.models import Author
from books.models import Log
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, TemplateView)
from django.urls import reverse_lazy


class Index(TemplateView):
    template_name = 'index.html'


class BookList(ListView):
    queryset = Book.objects.all()


class AuthorList(ListView):
    queryset = Author.objects.all()


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


class AuthorUpdate(UpdateView):
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


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books-list')


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors-list')


class LogsList(ListView):
    queryset = Log.objects.all()
