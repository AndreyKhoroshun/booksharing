from django import forms
from accounts.models import User
from accounts.tasks import send_activate_account_email
from django.contrib.auth.tokens import default_token_generator


class SighUpForm(forms.ModelForm):
    password1 = forms.CharField(min_length=6, widget=forms.PasswordInput())
    password2 = forms.CharField(min_length=6, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            self.add_error('password2', 'Passwords should match!')

        return cleaned_data

    def save(self, commit=True):
        instance: User = super().save(commit=False)
        instance.is_active = False
        instance.set_password(self.cleaned_data['password1'])

        if commit:
            instance.save()

        token = default_token_generator.make_token(instance)
        send_activate_account_email.delay(instance.username, token)

        return instance
