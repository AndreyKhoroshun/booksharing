from django.contrib import admin
import debug_toolbar
from django.urls import include, path
from accounts.views import MyProfileView, ContactUsView
from books import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('books/', include('books.urls')),
    path('accounts/my-profile/', MyProfileView.as_view(), name='my-profile'),
    path('accounts/contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('', views.Index.as_view(), name='index'),
    path('logs/', views.LogsList.as_view(), name='logs'),
    path('__debug__/', include(debug_toolbar.urls)),
]
