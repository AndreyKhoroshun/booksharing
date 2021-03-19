from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class ContactUs(models.Model):
    full_name = models.CharField(max_length=128)
    contact_to_email = models.EmailField()
    message = models.CharField(max_length=1024)
    created = models.DateField(auto_now_add=True)
