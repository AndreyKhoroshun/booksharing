from books.models import Book
from books.models import Author
from books.models import Log
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, TemplateView, View)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from books.forms import BookForm
from django.http import HttpResponse
from books.utils import display
import csv
import xlwt


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


class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    success_url = reverse_lazy('books:authors-list')
    fields = (
        'first_name',
        'last_name',
        'date_of_birth',
        'date_of_death',
        'country',
        'gender',
        'native_language',
    )


class BookUpdate(FormUserKwargMixin, UpdateView):
    model = Book
    success_url = reverse_lazy('books:my-books')
    form_class = BookForm


class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    success_url = reverse_lazy('books:authors-list')
    fields = (
        'first_name',
        'last_name',
        'date_of_birth',
        'date_of_death',
        'country',
        'gender',
        'native_language',
    )


class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books:list')


class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors-list')


class LogsList(ListView):
    queryset = Log.objects.all()


class DownloadCSVBookView(View):

    HEADERS = (
        'id',
        'title',
        'author.full_name',
        'author.get_full_name',
        'publish_year',
        'condition',
    )

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        writer = csv.writer(response)
        writer.writerow(self.HEADERS)
        for book in Book.objects.all().select_related('author').iterator():
            writer.writerow([
                display(book, header)
                for header in self.HEADERS
            ])
        return response


class DownloadXLSXBookView(View):

    HEADERS = (
        'id',
        'title',
        'author.full_name',
        'author.get_full_name',
        'publish_year',
        'condition',
    )

    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="somefilename.xls"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet("book_list")
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        for col_num in range(len(self.HEADERS)):
            ws.write(row_num, col_num, self.HEADERS[col_num], font_style)
        font_style = xlwt.XFStyle()
        data = Book.objects.all().select_related('author').iterator()
        for book in data:
            row_num = row_num + 1
            for col_num in range(len(self.HEADERS)):
                ws.write(row_num, col_num, display(book, self.HEADERS[col_num]), font_style)
        wb.save(response)
        return response
