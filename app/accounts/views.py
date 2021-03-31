from django.views.generic import UpdateView, CreateView, RedirectView
from accounts.models import User, ContactUs
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.tasks import send_contact_us_email
from accounts.forms import SighUpForm
from annoying.functions import get_object_or_None
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator


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


class SignUpView(CreateView):
    model = User
    success_url = reverse_lazy('index')
    form_class = SighUpForm
    template_name = 'accounts/signup.html'


class ActivateView(RedirectView):
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.pop('username')
        token = kwargs.pop('token')
        user = get_object_or_None(User, username=username, is_active=False)
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save(update_fields=('is_active', ))
            messages.add_message(self.request, messages.INFO, 'Your account is activated!')
        return super().get_redirect_url(*args, **kwargs)
