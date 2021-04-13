from books.models import Book, Author, Log, RequestBook
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, TemplateView, View, DetailView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from books.forms import BookForm
from django.http import HttpResponse
from books.utils import display
from django.shortcuts import redirect, get_object_or_404
from books import model_choices as mch
from django.contrib import messages
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

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.exclude(user=self.request.user)


class MyBooksList(LoginRequiredMixin, ListView):
    queryset = Book.objects.all().select_related('author')
    template_name = 'books/my_books.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class MyRequestedBooks(LoginRequiredMixin, ListView):
    queryset = RequestBook.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(recipient=self.request.user)


class RequestedBooks(LoginRequiredMixin, ListView):
    queryset = RequestBook.objects.all()
    template_name = 'books/requested_book_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(book__user=self.request.user)


class AuthorList(ListView):
    queryset = Author.objects.all()


class BookCreate(FormUserKwargMixin, CreateView):
    model = Book
    success_url = reverse_lazy('books:my-books')
    form_class = BookForm

    def get_success_url(self):
        messages.success(self.request, 'New book created')
        return super().get_success_url()


class BookInfo(DetailView):
    queryset = Book.objects.all().select_related('author')
    template_name = 'books/book_info.html'


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

    def get_success_url(self):
        messages.success(self.request, 'New author created')
        return super().get_success_url()


class BookUpdate(FormUserKwargMixin, UpdateView):
    model = Book
    success_url = reverse_lazy('books:my-books')
    form_class = BookForm

    def get_success_url(self):
        messages.success(self.request, 'Book edited')
        return super().get_success_url()


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

    def get_success_url(self):
        messages.success(self.request, 'Author edited')
        return super().get_success_url()


class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books:list')

    def get_success_url(self):
        messages.success(self.request, 'Book delete')
        return super().get_success_url()


class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors-list')


class RequestBookCreate(LoginRequiredMixin, View):

    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        if not RequestBook.objects.filter(book=book, recipient=request.user, status=mch.STATUS_IN_PROGRESS).exists():
            RequestBook.objects.create(book=book, recipient=request.user, status=mch.STATUS_IN_PROGRESS)
        return redirect('books:list')


class _ChangeRequestBaseView(LoginRequiredMixin, View):
    CURRENT_STATUS = None
    NEW_STATUS = None
    REDIRECT_NAME = None
    MESSAGE = None

    def get(self, request, request_id):
        request_obj = get_object_or_404(RequestBook, pk=request_id, status=self.CURRENT_STATUS)
        request_obj.status = self.NEW_STATUS
        request_obj.save(update_fields=('status',))

        if self.MESSAGE:
            messages.add_message(request, messages.INFO, self.MESSAGE)

        return redirect(self.REDIRECT_NAME)


class RequestBookConfirm(_ChangeRequestBaseView):
    CURRENT_STATUS = mch.STATUS_IN_PROGRESS
    NEW_STATUS = mch.STATUS_CONFIRMED
    REDIRECT_NAME = 'books:requested-books'
    MESSAGE = 'Book Request Was Confirmed!'


class RequestBookReject(_ChangeRequestBaseView):
    CURRENT_STATUS = mch.STATUS_IN_PROGRESS
    NEW_STATUS = mch.STATUS_REJECT
    REDIRECT_NAME = 'books:requested-books'
    MESSAGE = 'Book Request Was Rejected!'


class RequestBookSentViaEmail(_ChangeRequestBaseView):
    CURRENT_STATUS = mch.STATUS_CONFIRMED
    NEW_STATUS = mch.STATUS_SENT_TO_RECIPIENT
    REDIRECT_NAME = 'books:requested-books'


class RequestBookReceivedBook(_ChangeRequestBaseView):
    CURRENT_STATUS = mch.STATUS_SENT_TO_RECIPIENT
    NEW_STATUS = mch.STATUS_RECIPIENT_RECEIVED_BOOK
    REDIRECT_NAME = 'books:my-requested-books'


class RequestBookSentBackToOwner(_ChangeRequestBaseView):
    CURRENT_STATUS = mch.STATUS_RECIPIENT_RECEIVED_BOOK
    NEW_STATUS = mch.STATUS_SENT_BACK_TO_OWNER
    REDIRECT_NAME = 'books:my-requested-books'


class RequestBookOwnerReceivedBack(_ChangeRequestBaseView):
    CURRENT_STATUS = mch.STATUS_SENT_BACK_TO_OWNER
    NEW_STATUS = mch.STATUS_OWNER_RECEIVED_BACK
    REDIRECT_NAME = 'books:requested-books'


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
        for book in Book.objects.all().select_related('author').iterator():
            row_num += 1
            for col_num in range(len(self.HEADERS)):
                ws.write(row_num, col_num, display(book, self.HEADERS[col_num]), font_style)
        wb.save(response)
        return response
