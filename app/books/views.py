from books.models import Book
from books.models import Author
from books.models import Log
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, TemplateView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from books.forms import BookForm, AuthorForm


class FormUserKwargMixin:
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class Index(TemplateView):
    template_name = 'index.html'


class BookList(ListView):
    queryset = Book.objects.all().select_related('author', 'category')


class MyBooksList(LoginRequiredMixin, ListView):
    queryset = Book.objects.all().select_related('author')
    template_name = 'books/my_books.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class AuthorList(ListView):
    queryset = Author.objects.all()


class BookCreate(FormUserKwargMixin, CreateView):
    model = Book
    success_url = reverse_lazy('books:my-books')
    form_class = BookForm


class AuthorCreate(FormUserKwargMixin, CreateView):
    model = Author
    success_url = reverse_lazy('books:authors-list')
    form_class = AuthorForm


class BookUpdate(FormUserKwargMixin, UpdateView):
    model = Book
    success_url = reverse_lazy('books:my-books')
    form_class = BookForm


class AuthorUpdate(FormUserKwargMixin, UpdateView):
    model = Author
    success_url = reverse_lazy('books:authors-list')
    form_class = AuthorForm


class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books:list')


class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors-list')


class LogsList(ListView):
    queryset = Log.objects.all()
