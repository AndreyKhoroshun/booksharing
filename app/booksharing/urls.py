from django.contrib import admin
from django.urls import path

from books import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('books/list/', views.book_list),

    path('authors/list/', views.author_list),

    path('books/create/', views.book_create),

    path('authors/create/', views.author_create),

    path('books/update/<int:pk>/', views.book_update),

    path('authors/update/<int:pk>/', views.author_update),

]
