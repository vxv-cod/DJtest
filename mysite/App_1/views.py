from django.http import HttpResponse
from django.shortcuts import render

from App_1.backend import testTest


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    testTest.GO()
    return render(request, 'index.html')