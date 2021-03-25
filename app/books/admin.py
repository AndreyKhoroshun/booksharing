from django.contrib import admin
from books.models import RequestBook, Book, Author


class RequestBookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'recipient',
        'book',
        'created',
        'status',
    )
    readonly_fields = ('recipient', 'book')
    list_filter = ('status', 'created', )
    search_fields = ('recipient__username', 'recipient__last_name')

    def has_delete_permission(self, request, obj=None):
        return False


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'date_of_birth',
        'date_of_death',
        'country',
        'gender',
        'native_language',
    )
    readonly_fields = (
        'first_name',
        'last_name',
        'gender',
    )
    list_filter = ('country', 'gender', 'native_language')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'publish_year',
        'review',
        'condition',
        'category',
        'user',
        'author',
    )
    readonly_fields = (
        'publish_year',
        'category',
        'author',
    )
    list_filter = ('condition', 'category', )
    search_fields = ('title', 'category', 'author')


admin.site.register(RequestBook, RequestBookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
