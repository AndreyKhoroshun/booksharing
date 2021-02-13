from django.shortcuts import render
from django.http import HttpResponse

import string
import random


def gennerate_password(lenght: int = 10) -> str:
    password = ''
    for _ in range(lenght):
        password += random.choice(string.ascii_letters)
    return password


def hello_world(request):
    length = int(request.GET.get('length') or 10)
    password = gennerate_password(length)
    return HttpResponse(password)
