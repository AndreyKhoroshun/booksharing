from django.contrib import admin
import debug_toolbar
from django.urls import include, path
from accounts.views import MyProfileView, ContactUsView, SignUpView, ActivateView
from books import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('books/', include('books.urls')),
    path('accounts/my-profile/', MyProfileView.as_view(), name='my-profile'),
    path('accounts/contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/activate/<uuid:username>/<token>/', ActivateView.as_view(), name='activate'),
    path('', views.Index.as_view(), name='index'),
    path('logs/', views.LogsList.as_view(), name='logs'),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
