from django.contrib import admin
from django.urls import path

from books import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('books/list/', views.book_list, name='books-list'),
    path('authors/list/', views.author_list, name='authors-list'),
    path('books/create/', views.book_create, name='books-create'),
    path('authors/create/', views.author_create, name='authors-create'),
    path('books/update/<int:pk>/', views.book_update, name='books-update'),
    path('authors/update/<int:pk>/', views.author_update, name='authors-update'),
    path('books/delete/<int:pk>/', views.book_delete, name='books-delete'),
    path('authors/delete/<int:pk>/', views.author_delete, name='authors-delete'),

]
