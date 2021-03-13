from django import forms

from books.models import Book
from books.models import Author
from books.models import Category


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = (
            'first_name',
            'last_name',
            'date_of_birth',
            'date_of_death',
            'country',
            'gender',
            'native_language',
        )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
        )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'author',
            'title',
            'category',
            'publish_year',
            'review',
            'condition',
        )
