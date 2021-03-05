from django.contrib import admin

import debug_toolbar
from django.urls import include, path

from books import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('', views.Index.as_view(), name='index'),
    path('books/list/', views.BookList.as_view(), name='books-list'),
    path('authors/list/', views.AuthorList.as_view(), name='authors-list'),
    path('books/create/', views.BookCreate.as_view(), name='books-create'),
    path('authors/create/', views.AuthorCreate.as_view(), name='authors-create'),
    path('books/update/<int:pk>/', views.BookUpdate.as_view(), name='books-update'),
    path('authors/update/<int:pk>/', views.AuthorUpdate.as_view(), name='authors-update'),
    path('books/delete/<int:pk>/', views.BookDelete.as_view(), name='books-delete'),
    path('authors/delete/<int:pk>/', views.AuthorDelete.as_view(), name='authors-delete'),
    path('logs/', views.LogsList.as_view(), name='logs'),
    path('__debug__/', include(debug_toolbar.urls)),
]
