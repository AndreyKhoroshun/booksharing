from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [

    path('books-list/', views.BookList.as_view(), name='list'),
    path('author-list/', views.AuthorList.as_view(), name='authors-list'),
    path('books-create/', views.BookCreate.as_view(), name='create'),
    path('authors-create/', views.AuthorCreate.as_view(), name='authors-create'),
    path('books-update/<int:pk>/', views.BookUpdate.as_view(), name='update'),
    path('authors-update/<int:pk>/', views.AuthorUpdate.as_view(), name='authors-update'),
    path('books-delete/<int:pk>/', views.BookDelete.as_view(), name='delete'),
    path('authors-delete/<int:pk>/', views.AuthorDelete.as_view(), name='authors-delete'),

]