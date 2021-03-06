from django.views.generic import UpdateView
from accounts.models import User
from django.urls import reverse_lazy


class MyProfileView(UpdateView):
    model = User
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
    )
