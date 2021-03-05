from django.contrib import admin

import debug_toolbar
from django.urls import include, path

from books import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('', views.index, name='index'),
    path('books/list/', views.book_list, name='books-list'),
    path('authors/list/', views.author_list, name='authors-list'),
    path('books/create/', views.BookCreate.as_view(), name='books-create'),
    path('authors/create/', views.AuthorCreate.as_view(), name='authors-create'),
    path('books/update/<int:pk>/', views.BookUpdate.as_view(), name='books-update'),
    path('authors/update/<int:pk>/', views.AuthorUpdate.as_view(), name='authors-update'),
    path('books/delete/<int:pk>/', views.book_delete, name='books-delete'),
    path('authors/delete/<int:pk>/', views.author_delete, name='authors-delete'),
    path('logs/', views.logs_list, name='logs'),
    path('__debug__/', include(debug_toolbar.urls)),
]
