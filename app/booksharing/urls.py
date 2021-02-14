from django.contrib import admin
from django.urls import path

from books import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('book/list/', views.book_list),

    path('author/list/', views.author_list),

]
