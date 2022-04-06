from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):  # index(request) is a convention
    return HttpResponse('Olá Mundo')


