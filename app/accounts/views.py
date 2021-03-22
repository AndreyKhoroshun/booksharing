from django.views.generic import UpdateView, CreateView
from accounts.models import User, ContactUs
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.tasks import send_contact_us_email


class MyProfileView(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
    )

    def get_object(self, queryset=None):
        return self.request.user


class ContactUsView(CreateView):
    model = ContactUs
    success_url = reverse_lazy('index')
    fields = (
        'full_name',
        'contact_to_email',
        'message',
    )

    def form_valid(self, form):
        response = super().form_valid(form)
        send_contact_us_email.delay(form.cleaned_data)
        return response
